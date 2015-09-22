# -*- coding: utf-8 -*-
##################################################
# rdryan@sina.com
# Copyright (c) 2015
##################################################
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from yelp.items import YelpItem
from urlparse import urlparse

class YelpatSpider(scrapy.Spider):
    name = "yelpat"
    allowed_domains = ["yelp.at"]
    start_urls = (
        #'http://www.yelp.at/',
        'http://www.yelp.at/search?find_loc=wien&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Graz&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Linz&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Klagenfurt&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Salzburg&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Innsbruck&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Wels&start=0&attrs=RestaurantsDelivery',        
        #'http://www.yelp.at/search?find_loc=Villach&start=0&attrs=RestaurantsDelivery',        
    )

    def parse(self, response):
        sel = Selector(response)
        #item = YelpItem()
        infos = sel.xpath('//a[@class="biz-name"]')
        
        
        for info in infos:
            name = info.xpath('text()').extract()

            #if 'Vietthao' in name:
            if True:
                url = ''.join(info.xpath('@href').extract()).strip()
                print url
                print name

                url_i = "http://%s%s" %(urlparse(response.url).hostname, url)
                yield Request(url_i, callback=self.parse_items)
                
        
        next = sel.xpath('//a[@class="page-option prev-next next"]/@href').extract()
        for i in next:
            url_i = "http://%s%s" %(urlparse(response.url).hostname, i)
            yield Request(url_i, callback=self.parse)
        
    def parse_items(self, response):
        sel = Selector(response)
        item = YelpItem()

        item['name'] = ''.join(sel.xpath('//h1[@class="biz-page-title embossed-text-white shortenough"]//text()').extract()).strip()
        
        item['category'] = ''.join(sel.xpath('//span[@class="category-str-list"]//a//text()').extract()).strip()
        
        item['ratevalue'] = ''.join(sel.xpath('//div[@class="biz-page-header-left"]//meta[@itemprop="ratingValue"]//@content').extract()).strip()
        
        item['reviewcount'] = ''.join(sel.xpath('//span[@itemprop="reviewCount"]//text()').extract()).strip()

        item['address'] = ''.join(sel.xpath('//span[@itemprop="streetAddress"]//text()').extract()).strip()

        item['postcode'] = ''.join(sel.xpath('//span[@itemprop="postalCode"]//text()').extract()).strip()

        item['city'] = ''.join(sel.xpath('//span[@itemprop="addressLocality"]//text()').extract()).strip()
        
        item['area'] = ''.join(sel.xpath('//span[@class="neighborhood-str-list"]//text()').extract()).strip()
        
        item['telephone'] = ''.join(sel.xpath('//span[@itemprop="telephone"]//text()').extract()).strip()
        
        item['website'] = ''.join(sel.xpath('//div[@class="biz-website"]//a//text()').extract())
        
        item['price'] = ''.join(sel.xpath('//dd[@class="nowrap price-description"]//text()').extract()).strip()
        #item['price'] = sel.xpath('//dd[@class="nowrap price-description"]//text()').extract()
        
        
        
        #pass
        yield item
        
