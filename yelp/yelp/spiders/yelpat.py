# -*- coding: utf-8 -*-
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
    )

    def parse(self, response):
        sel = Selector(response)
        #item = YelpItem()
        infos = sel.xpath('//a[@class="biz-name"]')
        
        
        for info in infos:
            name = info.xpath('text()').extract()

            if 'Vietthao' in name:
                url = ''.join(info.xpath('@href').extract()).strip()
                print url
                #print info.xpath('text()').extract()
                print name

                url_i = "http://%s%s" %(urlparse(response.url).hostname, url)
                yield Request(url_i, callback=self.parse_items)
                
        
        #    item['name'] = ''.join(info.xpath('li[@class="yd-jig-service-dl-info-name"]/a/text()').extract()).strip()
        
        #for name in names:
            #print '======== name:' , item['name'].encode('utf-8')
            #print '     === open:' , item['openings'].encode('utf-8')

            #yield item

    def parse_items(self, response):
        sel = Selector(response)
        item = YelpItem()

        item['name'] = ''.join(sel.xpath('//h1[@class="biz-page-title embossed-text-white shortenough"]//text()').extract()).strip()
        
        item['ratevalue'] = ''.join(sel.xpath('//div[@class="biz-page-header-left"]//meta[@itemprop="ratingValue"]//@content').extract()).strip()
        
        item['reviewcount'] = ''.join(sel.xpath('//span[@itemprop="reviewCount"]//text()').extract()).strip()

        item['streetaddr'] = ''.join(sel.xpath('//span[@itemprop="streetAddress"]//text()').extract()).strip()

        item['postcode'] = ''.join(sel.xpath('//span[@itemprop="postalCode"]//text()').extract()).strip()

        item['addrlocality'] = ''.join(sel.xpath('//span[@itemprop="addressLocality"]//text()').extract()).strip()
        
        item['telephone'] = ''.join(sel.xpath('//span[@itemprop="telephone"]//text()').extract()).strip()
        
        #item['price'] = ''.join(sel.xpath('//dd[@class="nowrap price-description"]//text()').extract()).strip()
        item['price'] = sel.xpath('//dd[@class="nowrap price-description"]//text()').extract()
        
        #item['website'] = ''.join(sel.xpath('//span[@itemprop="WebSite"]//text()').extract())
        #print "    ====", item['website']
        
        
        #pass
        yield item
        
