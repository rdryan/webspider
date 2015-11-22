# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from craigslist.items import CraigslistItem
from scrapy.http import Request
from urlparse import urlparse
import urllib
import re

class CraigslistSpider(CrawlSpider):
    name = "craigslist_spider"
    allowed_domains = ["craigslist.org","craigslist.com","craigslist.com.cn","craigslist.hk"]
    start_urls = (
        #'http://www.craigslist.org/',
        'http://sfbay.craigslist.org/search/fud?postedToday=1',
        'http://losangeles.craigslist.org/search/fud?postedToday=1',
        'http://newyork.craigslist.org/search/fud?postedToday=1',
        'http://seattle.craigslist.org/search/fud?postedToday=1',
        'http://chicago.craigslist.org/search/fud?postedToday=1',
        'http://orangecounty.craigslist.org/search/fud?postedToday=1',
        'http://sandiego.craigslist.org/search/fud?postedToday=1',
        'http://washingtondc.craigslist.org/search/fud?postedToday=1',
        'http://boston.craigslist.org/search/fud?postedToday=1',
        'http://portland.craigslist.org/search/fud?postedToday=1',
        'http://atlanta.craigslist.org/search/fud?postedToday=1',
        'http://phoenix.craigslist.org/search/fud?postedToday=1',
        'http://dallas.craigslist.org/search/fud?postedToday=1',
        'http://denver.craigslist.org/search/fud?postedToday=1',
        'http://miami.craigslist.org/search/fud?postedToday=1',
        'http://inlandempire.craigslist.org/search/fud?postedToday=1',
        'http://sacramento.craigslist.org/search/fud?postedToday=1',
        'http://austin.craigslist.org/search/fud?postedToday=1',
        'http://minneapolis.craigslist.org/search/fud?postedToday=1',
        'http://philadelphia.craigslist.org/search/fud?postedToday=1',
        'http://newjersey.craigslist.org/search/fud?postedToday=1',
        'http://houston.craigslist.org/search/fud?postedToday=1',
        'http://tampa.craigslist.org/search/fud?postedToday=1',
        'http://orlando.craigslist.org/search/fud?postedToday=1',
        'http://raleigh.craigslist.org/search/fud?postedToday=1',
        'http://cnj.craigslist.org/search/fud?postedToday=1',
        'http://lasvegas.craigslist.org/search/fud?postedToday=1',
        'http://baltimore.craigslist.org/search/fud?postedToday=1',
        'http://charlotte.craigslist.org/search/fud?postedToday=1',
    )

    rules = (
            # Rule to go to each post
            Rule(LinkExtractor(
                    restrict_xpaths='//a[@class="hdrlnk"]',
                    canonicalize=True,
                ), callback='parsePost'),
            
            #Rule(LinkExtractor(
            #        restrict_xpaths='//a[@class="showcontact"]',
            #        canonicalize=True,
            #    ), callback='parsePost'),
            
            Rule(LinkExtractor(
                    restrict_xpaths='//a[@class="button next"]',
                    canonicalize=True,
                ), follow=True),
           
                    
            )
                    
    def parsePhoneNumber(self, content):
        #m = re.findall("\d+-\d+-\d+",content)       
        #m += re.findall("\d+[-| |(|)|.|/]\d+[-| |(|)|.|/]\d+",content)       
        #m = re.findall("\d{1,3}[-| |.|/]\d{1,3}[-| |.|/]\d{1,4}",content)       
        content = content.replace(' ','')
        content = content.replace('(','')
        content = content.replace(')','')
        content = content.replace('-','')
        content = content.replace('.','')
        content = content.replace(',','')
       
        m = re.findall("\d{10}",content)       
        
        return m

    ''' 
    def parseImage(self, url):
        image_name = "./images/" + url.split('/').pop(-1)
        print image_name
        yield urllib.urlretrieve(url,image_name)
        
        return
    '''    

    def parsePost(self, response):
        sel = Selector(response)
        item = CraigslistItem()
        
        #content = sel.xpath('//section[@id="postingbody"]/a[@class="showcontact"]/@href').extract()
        #item["content"] = content.replace('\n','').replace('\s+',' ')
        
        contact = sel.xpath('//a[@class="showcontact"]/@href').extract() 
        if len(contact) > 0:
            url = "http://%s%s" %(urlparse(response.url).hostname, contact)
            yield Request(url, callback=self.parsePost)

        
        content = ''.join(sel.xpath('//section[@id="postingbody"]/text()').extract())
        phoneNumber = self.parsePhoneNumber(content)
        
        image_url = sel.xpath('//figure[@class="iw oneimage"]//img/@src').extract()
        #phoneNumber += self.parseImage(image_url)

        item["image_url"] = image_url
        
        #if len(phoneNumber) == 0:
        #    return
        
        item['phoneNumber'] = phoneNumber
        yield item

