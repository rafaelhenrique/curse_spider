# -*- coding: utf-8 -*-
import scrapy
from curse_spider.my_addons import MY_ADDONS
from curse_spider.items import UrlItem


class AddonsSpider(scrapy.Spider):
    name = "addons"
    allowed_domains = ["www.curse.com"]
    start_urls = MY_ADDONS

    def parse(self, response):
        base_url = 'https://www.curseforge.com'
        url = response.xpath(
            r'//*[@class="download__link"]'
            r'/@href').extract_first()

        item = UrlItem()
        item['url'] = base_url + url
        return item
