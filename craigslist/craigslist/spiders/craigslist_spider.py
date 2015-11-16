# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from craigslist.items import CraigslistItem

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
                    
    
    def parsePost(self, response):
        sel = Selector(response)
        item = CraigslistItem()
        
        #content = sel.xpath('//section[@id="postingbody"]/a[@class="showcontact"]/@href').extract()
        content = sel.xpath('//section[@id="postingbody"]/text()').extract()[0]
        #item["content"] = content.replace('\n','').replace('\s+',' ')
        
        image_url = ''.join(sel.xpath('//figure[@class="iw oneimage"]//img/@src').extract())
        item["image_url"] = image_url
        
        return item

