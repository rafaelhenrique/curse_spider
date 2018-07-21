# -*- coding: utf-8 -*-

import scrapy
import requests
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem


class AddonsPipeline(FilesPipeline):

    def handle_redirect(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            url = response.url
        return url

    def get_media_requests(self, item, info):
        url_location = self.handle_redirect(**item)
        if not url_location:
            yield scrapy.Request(**item)
        yield scrapy.Request(url=url_location)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item dont contain files")
        item['file_paths'] = file_paths
        return item
