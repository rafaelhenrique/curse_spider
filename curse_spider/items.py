# -*- coding: utf-8 -*-

import scrapy


class UrlItem(scrapy.Item):
    url = scrapy.Field()
    file_paths = scrapy.Field()
