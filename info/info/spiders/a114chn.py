# -*- coding: utf-8 -*-
import scrapy


class A114chnSpider(scrapy.Spider):
    name = "114chn"
    allowed_domains = ["114chn.com"]
    start_urls = (
        'http://www.114chn.com/',
    )

    def parse(self, response):
        pass
