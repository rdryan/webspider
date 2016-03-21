# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from realestate.items import RealestateItem

class McgrathSpiderSpider(scrapy.Spider):
    name = "mcgrath_spider"
    allowed_domains = ["mcgrath.com.au"]
    start_urls = (
        #'http://www.mcgrath.com.au/',
        'https://www.mcgrath.com.au/rent/offices/nsw/sutherland-shire/engadine/47463',
        'https://www.mcgrath.com.au/rent/offices/nsw/sutherland-shire/engadine/47464',
        'https://www.mcgrath.com.au/rent/offices/nsw/sutherland-shire/engadine/47465',
    )

    def parse(self, response):
        item = RealestateItem()
        sel = Selector(response)
        
        item['name'] = ''.join(sel.xpath('//section[@id="_mg_listing_detail"]//h1/text()').extract())
        
        #item['price'] = ''.join(sel.xpath('///section[@id="_mg_listing_detail"]/div/div[1]/div[1]/p/text()').extract())
        item['price'] = ''.join(sel.xpath('///section[@id="_mg_listing_detail"]/div/div[2]/div[2]/p[3]/text()').extract())
        
        item['url'] = response.url

        yield item
