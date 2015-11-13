# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from image.items import ImageItem
from urlparse import urlparse

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        #'http://www.example.com/',
        'http://product.auto.163.com/price/p10to15/',
    )

    def parse(self, response):
        sel = Selector(response)
        #print response.url
        #print response.body
        
        infos = sel.xpath('//ul[@class="autocardlst clearfix"]//div[@class="price"]').extract()
        
        for info in infos:
            print info

        pass
