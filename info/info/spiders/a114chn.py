# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from info.items import InfoItem
from urlparse import urlparse

class A114chnSpider(CrawlSpider):
    name = "a114chn"
    allowed_domains = ["114chn.com"]
    start_urls = (
        #'http://www.114chn.com/',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=11&pattern=2&page=1',
    )

    rules = (
            # Rule to go to each company
            Rule(LinkExtractor(
                    restrict_xpaths='//div[@class="left-col"]//div[@class="f"]//a',
                    canonicalize=True,
                ), callback='parseCompany'),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//div[@class="p"]//a',
                    canonicalize=True,
                ), follow=True),
           
                    
            )
    
    
    def parseCompany22(self, response):
        #print response.body
        #print response.url
        sel = Selector(response)
        
        contact_url = sel.xpath('//a[@id="contactMenu"]/@href').extract()[0]
        
        contact_url = "http://%s%s" %(urlparse(response.url).hostname, contact_url)
        
        yield Request(contact_url, callback=self.parse_items)

    #def parse_items(self, response):
    def parseCompany(self, response):
        #print "+++++++++", response.url
        sel = Selector(response)
        item = InfoItem()
        
        #name = sel.xpath('//span[@class="company-name fl"]/text()').extract()[0]
        #contact = sel.xpath('//div[@class="bor-t"]/span/text()').extract()[0]
        name = ''.join(sel.xpath('//table[@class="tablebg"]//text()').extract())
        print name
        #print contact
        item["name"] = name.encode('utf-8')
        #item["contact"] = contact.encode('utf-8')

        #return item
        yield item
        
        

