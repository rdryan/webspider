# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from info.items import InfoItem
from urlparse import urlparse

class EbnewSpider(CrawlSpider):
    name = "ebnew_spider"
    allowed_domains = ["ebnew.com", "yuecai.com"]
    start_urls = [
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=31*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=31*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=32*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=32*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=33*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=33*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=11*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=11*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=12*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=12*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=13*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=13*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=14*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=14*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=15*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=15*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=21*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=21*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
        "http://www.ebnew.com/searchCompany.view?&industrys=&zType=1&zones=44*&workPattern=&zoneStr=&!zoneStr&key=&userType=&selkey=&zones=44*&businesType=1&queryShort=0&selkey=&approved=0&currentPage=1",
    ]

    rules = (
            # Rule to go to each company
            Rule(LinkExtractor(
                    restrict_xpaths='//a[@class="jc sl ydwbj"]',
                    canonicalize=True,
                ), callback='parseCompany'),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//a[contains(@href,"currentPage=")]',
                    canonicalize=True,
                ), follow=True),
           
                    
            )
    
    
    def parseCompany(self, response):
        #print response.body
        #print response.url
        sel = Selector(response)
        
        contact_url = sel.xpath('//a[@id="contactMenu"]/@href').extract()[0]
        
        contact_url = "http://%s%s" %(urlparse(response.url).hostname, contact_url)
        
        yield Request(contact_url, callback=self.parse_items)

    def parse_items(self, response):
        #print "+++++++++", response.url
        sel = Selector(response)
        item = InfoItem()
        
        #name = sel.xpath('//span[@class="company-name fl"]/text()').extract()[0]
        #contact = sel.xpath('//div[@class="bor-t"]/span/text()').extract()[0]
        name = sel.xpath('//meta[@name="description"]/@content').extract()[0]
        print name
        #print contact
        item["name"] = name.encode('utf-8')
        #item["contact"] = contact.encode('utf-8')

        #return item
        yield item
        
        

