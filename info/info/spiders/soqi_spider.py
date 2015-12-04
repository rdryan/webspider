# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from info.items import InfoItem
from urlparse import urlparse
from bs4 import BeautifulSoup
import re


class InfoSpider(CrawlSpider):
    name = "soqi_spider"
    allowed_domains = ["soqi.cn"]
    start_urls = [
        "http://www.soqi.cn/search.xhtml?keywords=%E5%B7%A5%E4%B8%9A&page=1&city=100000&regCapital=&search_type=1",
        "http://www.soqi.cn/search.xhtml?keywords=%E5%B7%A5%E4%B8%9A&page=1&city=100000&regCapital=&search_type=2",
        "http://www.soqi.cn/search.xhtml?keywords=%E5%B7%A5%E4%B8%9A&page=1&city=100000&regCapital=&search_type=3",
        "http://www.soqi.cn/search.xhtml?keywords=%E5%B7%A5%E4%B8%9A&page=1&city=100000&regCapital=&search_type=4",
        "http://www.soqi.cn/search.xhtml?keywords=%E5%85%AC%E5%8F%B8&page=1&city=100000&regCapital=&search_type=1",
    ]

    rules = (
            # Rule to go to each company
            Rule(LinkExtractor(
                    #restrict_xpaths='//a[@target="_blank"]',
                    restrict_xpaths='//div[@class="itemblocks"]//a',
                    canonicalize=True,
                #), follow=True),
                ), callback='parseCompany'),
            
            # next page
            #Rule(LinkExtractor(
            #        #restrict_xpaths='//a[contains(@onclick,"return")]',
            #        restrict_xpaths='//div[@class="topcity"]',
            #        canonicalize=True,
            #    ), follow=True),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//nav[@class="page btm_page"]//a',
                    canonicalize=True,
                ), follow=True),
                #), callback='parseCompany'),
           
                    
            )
   

    def cleanText(self,text):
        soup = BeautifulSoup(text,'html.parser')
        text = soup.get_text();
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+",' ',text).strip()
        return text 
    
    def parseCompany(self, response):
    #def parse(self, response):
        #print response.body
        #print "======================="
        #print response.url
        sel = Selector(response)
        item = InfoItem()
        
        #infos = sel.xpath('//dl[contains(@id,"info")]')
        #print infos

        #for info in infos:
        name = sel.xpath('//span[@class="detail_tit"]/text()').extract()
        contact = ''.join(sel.xpath('//div[@id="showAway"]//text()').extract())
        contact = self.cleanText(contact)
        
        if contact == '':
            return

        item['name'] = name
        item['contact'] = contact
        #item['url'] = response.url
        
        yield item
