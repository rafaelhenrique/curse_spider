# -*- coding: utf-8 -*-
import scrapy
from curse_spider.my_addons import MY_ADDONS
from curse_spider.items import UrlItem


class AddonsSpider(scrapy.Spider):
    name = "addons"
    allowed_domains = ["www.curse.com"]
    start_urls = MY_ADDONS

    def parse(self, response):
        url = response.xpath(
            r'//*[@id="file-download"]'
            r'/div[1]/p/a'
            r'/@data-href').extract_first()

        item = UrlItem()
        item['url'] = url
        return item
