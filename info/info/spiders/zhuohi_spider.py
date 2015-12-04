# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from info.items import InfoItem
from urlparse import urlparse

class InfoSpider(CrawlSpider):
    name = "zhuohi_spider"
    allowed_domains = ["zhuohi.com"]
    start_urls = [
        "http://www.zhuohi.com/sitemap.html",
        #"http://www.zhuohi.com/results_T1__-4E91-5357-7701_1.html",
    ]

    rules = (
            # Rule to go to each company
            Rule(LinkExtractor(
                    #restrict_xpaths='//a[@target="_blank"]',
                    restrict_xpaths='//div[@class="topcity"]//dl[@id="clist"]//a',
                    canonicalize=True,
                ), follow=True),
                #), callback='parseCompany'),
            
            # next page
            #Rule(LinkExtractor(
            #        #restrict_xpaths='//a[contains(@onclick,"return")]',
            #        restrict_xpaths='//div[@class="topcity"]',
            #        canonicalize=True,
            #    ), follow=True),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//div[@class="pageBox"]/a',
                    canonicalize=True,
                ), callback='parseCompany'),
           
                    
            )
    
    
    def parseCompany(self, response):
    #def parse(self, response):
        #print response.body
        #print "======================="
        #print response.url
        sel = Selector(response)
        item = InfoItem()
        
        infos = sel.xpath('//dl[contains(@id,"info")]')
        #print infos

        for info in infos:
            name = info.xpath('.//dt[@class="resComName"]/a/text()').extract()
            contact = ''.join(info.xpath('.//dd[@class="impotantInfo"]/text()').extract())
            
            item['name'] = name
            item['contact'] = contact
            #item['url'] = response.url
            
            yield item
