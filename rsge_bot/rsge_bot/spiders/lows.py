# -*- coding: utf-8 -*-
import scrapy


class LowsSpider(scrapy.Spider):
    name = 'lows'
    allowed_domains = ['services.runescape.com']
    start_urls = ['http://services.runescape.com/']

    def parse(self, response):
        pass
