# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from craigslist.items import CraigslistItem
from urlparse import urlparse
import re

class CraigslistSpider(CrawlSpider):
    name = "craigslist_spider"
    allowed_domains = ["craigslist.org","craigslist.com","craigslist.com.cn","craigslist.hk"]
    start_urls = (
        #'http://www.craigslist.org/',
        #'http://guangzhou.craigslist.com.cn/search/lbs',
        #'http://guangzhou.craigslist.com.cn/search/edu',
        'http://newyork.craigslist.org/search/lbs',
    )

    rules = (
            # Rule to go to each post
            Rule(LinkExtractor(
                    restrict_xpaths='//a[@class="hdrlnk"]',
                    canonicalize=True,
                ), callback='parsePost'),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//a[@class="button next"]',
                    canonicalize=True,
                ), follow=True),
           
                    
            )
                    
    
    def parseContact(self, response):
        sel = Selector(response)
        item = CraigslistItem()
        content = ''.join(sel.xpath('//body/text()').extract()).replace('\n','').replace('\s+',' ')
        item["content"] = content
        
        phone_num = re.findall('\d+-+\d+-+\d+',content)
        phone_num += re.findall('\(\d+\)-+\d+-+\d+',content)
        item["phone_num"] = phone_num
        
        yield item


    def parsePost(self, response):
        sel = Selector(response)
        item = CraigslistItem()
        
        content = ''.join(sel.xpath('//section[@id="postingbody"]/text()').extract()).replace('\n','').replace('\s+',' ')
        item["content"] = content
        
        contact_urls = sel.xpath('//section[@id="postingbody"]/a[@class="showcontact"]/@href').extract()

        if len(contact_urls) > 0:
            contact_url = contact_urls[0]
            url = "http://%s%s" %(urlparse(response.url).hostname, contact_url)
            yield Request(url, callback=self.parseContact)

        phone_num = re.findall('\d+-+\d+-+\d+',content)
        phone_num += re.findall('\(\d+\)-+\d+-+\d+',content)
        item["phone_num"] = phone_num
        
        image_url = ''.join(sel.xpath('//figure[@class="iw oneimage"]//img/@src').extract())
        item["image_url"] = image_url
        
        yield item
    
