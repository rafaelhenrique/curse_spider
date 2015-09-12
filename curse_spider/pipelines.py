# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class CurseSpiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem


class AddonsPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(**item)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item dont contain files")
        item['file_paths'] = file_paths
        return item
