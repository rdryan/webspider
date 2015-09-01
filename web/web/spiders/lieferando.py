# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from web.items import WebItem


class LieferandoSpider(scrapy.Spider):
    name = "lieferando"
    allowed_domains = ["lieferando.de"]
    start_urls = (
        #'https://www.lieferando.de',
        'https://www.lieferando.de/lieferservice-berlin-12305#!',
    )

    def parse(self, response):
        sel = Selector(response)
        item = WebItem()
        infos = sel.xpath('//ul[@class="yd-jig-service-dl-info"]')
        for info in infos:
            item['name'] = ''.join(info.xpath('li[@class="yd-jig-service-dl-info-name"]/a/text()').extract()).strip()
            item['food'] = ''.join(info.xpath('li[@class="yd-jig-service-dl-info-food"]/text()').extract()).strip()
            item['openings'] = ''.join(info.xpath('li[@class="yd-jig-service-dl-info-openings"]/text()').extract()).strip()
        
        #for name in names:
            #print '======== name:' , item['name'].encode('utf-8')
            #print '     === food:' , item['food'].encode('utf-8')
            #print '     === open:' , item['openings'].encode('utf-8')

            yield item

        #pass
