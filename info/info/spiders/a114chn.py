# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from info.items import InfoItem
from urlparse import urlparse
import re
from bs4 import BeautifulSoup


class A114chnSpider(CrawlSpider):
    name = "a114chn"
    allowed_domains = ["114chn.com"]
    start_urls = (
        #'http://www.114chn.com/',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=11&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=13&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=14&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=15&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=21&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=22&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=23&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=32&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=33&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=34&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=35&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=36&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=37&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=41&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=42&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=43&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=44&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=45&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=46&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=50&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=51&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=52&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=53&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=54&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=61&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=62&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=63&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=64&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A&areaid=65&pattern=2&page=1',
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

    def cleanText(self,text):
        soup = BeautifulSoup(text,'html.parser')
        text = soup.get_text();
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+",' ',text).strip()
        return text 

    #def parse_items(self, response):
    def parseCompany(self, response):
        #print "+++++++++", response.url
        sel = Selector(response)
        item = InfoItem()
        
        #name = sel.xpath('//span[@class="company-name fl"]/text()').extract()[0]
        #contact = sel.xpath('//div[@class="bor-t"]/span/text()').extract()[0]
        name = ''.join(sel.xpath('//table[@class="tablebg"]//text()').extract())
        #print name
        #print contact
        item["name"] = self.cleanText(name)
        #item["contact"] = contact.encode('utf-8')

        #return item
        yield item
        
        

