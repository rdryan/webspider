# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from craigslist.items import CraigslistItem
from scrapy.http import Request
from urlparse import urlparse
#from selenium import webdriver
#from time import sleep
import urllib
import re

class CraigslistSpider(CrawlSpider):
#class CraigslistSpider(Spider):
    name = "craigslist_spider"
    allowed_domains = ["craigslist.org","craigslist.com","craigslist.com.cn","craigslist.hk"]
    start_urls = (
        #'http://www.craigslist.org/',
        #'http://sfbay.craigslist.org/sfc/fud/5314826222.html',
        #'http://sfbay.craigslist.org/search/fud?postedToday=1',
        'http://losangeles.craigslist.org/search/fud?postedToday=1',
        #'http://newyork.craigslist.org/search/fud?postedToday=1',
        #'http://seattle.craigslist.org/search/fud?postedToday=1',
        #'http://chicago.craigslist.org/search/fud?postedToday=1',
        #'http://orangecounty.craigslist.org/search/fud?postedToday=1',
        #'http://sandiego.craigslist.org/search/fud?postedToday=1',
        #'http://washingtondc.craigslist.org/search/fud?postedToday=1',
        #'http://boston.craigslist.org/search/fud?postedToday=1',
        #'http://portland.craigslist.org/search/fud?postedToday=1',
        #'http://atlanta.craigslist.org/search/fud?postedToday=1',
        #'http://phoenix.craigslist.org/search/fud?postedToday=1',
        #'http://dallas.craigslist.org/search/fud?postedToday=1',
        #'http://denver.craigslist.org/search/fud?postedToday=1',
        #'http://miami.craigslist.org/search/fud?postedToday=1',
        #'http://inlandempire.craigslist.org/search/fud?postedToday=1',
        #'http://sacramento.craigslist.org/search/fud?postedToday=1',
        #'http://austin.craigslist.org/search/fud?postedToday=1',
        #'http://minneapolis.craigslist.org/search/fud?postedToday=1',
        #'http://philadelphia.craigslist.org/search/fud?postedToday=1',
        #'http://newjersey.craigslist.org/search/fud?postedToday=1',
        #'http://houston.craigslist.org/search/fud?postedToday=1',
        #'http://tampa.craigslist.org/search/fud?postedToday=1',
        #'http://orlando.craigslist.org/search/fud?postedToday=1',
        #'http://raleigh.craigslist.org/search/fud?postedToday=1',
        #'http://cnj.craigslist.org/search/fud?postedToday=1',
        #'http://lasvegas.craigslist.org/search/fud?postedToday=1',
        #'http://baltimore.craigslist.org/search/fud?postedToday=1',
        #'http://charlotte.craigslist.org/search/fud?postedToday=1',
    )

    #use proxy, if not use, comment it out
    service_args = [
        #'--proxy=127.0.0.1:8087',
        #'--proxy=xx.xx.13.122:3128',
        '--proxy-type=https',
        '--load-images=false',
        '--disk-cache=true',
        ]

    #driver = webdriver.PhantomJS(service_args=service_args)
    #driver = webdriver.PhantomJS()
   
    
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
    
    
    def parse22222(self, response):
        self.driver.get(response.url)
        el = Selector(text=self.driver.page_source).xpath('//a[@class="hdrlnk"]/@href').extract()
        requestList=[]
        for r in el:
            requestList.append(Request(response.urljoin(r), callback=self.parsePost))

        el = Selector(text=self.driver.page_source).xpath('//a[@class="button next"]/@href').extract()
        for r in el:
            requestList.append(Request(response.urljoin(r)))

        if len(requestList)>0:
            return requestList
        
        self.driver.close()
    
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
    #def parse(self, response):
        sel = Selector(response)
        #self.driver.get(response.url)
        #item = CraigslistItem()
        
        #contact = sel.xpath('//a[@class="showcontact"]/@href').extract() 
        #if len(contact) > 0:
        #    url = "http://%s%s" %(urlparse(response.url).hostname, contact)
        #    yield Request(url, callback=self.parsePost)
        #print self.driver.page_source
            
        #self.driver.find_element_by_xpath('//button[@class="reply_button js-only"]').click
        
        #print self.driver.page_source.encode('utf-8')

        #self.driver.save_screenshot("./tttt.png")

        #el = Selector(text=self.driver.page_source)
        #email = el.xpath('//ul[@class="pad"]//a/text()').extract()
        #print email
        #self.driver.close()
        
        #print self.driver.page_source 
        
        reply = ''.join(sel.xpath('//a[@id="replylink"]/@href').extract())
        yield Request(response.urljoin(reply), callback=self.parseContact )
        
        #content = ''.join(sel.xpath('//section[@id="postingbody"]/text()').extract())
        #item["content"] = content.replace('\n','').replace('\s+',' ')
        
        #phoneNumber = self.parsePhoneNumber(content)
        #phoneNumber += self.parseImage(image_url)
        #item['phone_num'] = phoneNumber
        
        #image_url = sel.xpath('//figure[@class="iw oneimage"]//img/@src').extract()
        #item["image_url"] = image_url
        
        #if len(phoneNumber) == 0:
        #    return
        
        #yield item

    def parseContact(self, response):
        #print response.url
        #print response.body
        
        sel = Selector(response)
        item = CraigslistItem()
        
        email = sel.xpath('//a[@class="mailapp"]//text()').extract()
        item['email'] = email

        phoneNumber = ''.join(sel.xpath('//a[@class="mobile-only replytellink"]/@href').extract()).replace("tel:","")
        item['phone_num'] = phoneNumber
        
        return item
        
