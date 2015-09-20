# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from web.items import WebItem
import urlparse


class CnlinfoSpider(scrapy.Spider):
    name = "cnlinfo"
    allowed_domains = ["114chn.com"]
    start_urls = (
        #ÉÏº£
        #'http://so.cnlinfo.net/gongsi/one_301/pro_440000/1.htm',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=1',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=2',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=3',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=4',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=5',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=6',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=7',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=8',
        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=9',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=10',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=11',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=12',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=13',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=14',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=15',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=16',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=17',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=18',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=19',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=20',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=21',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=22',
#        'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=23',
        
    )
    
    def parse(self, response):
        #print "body ----------", response.body.decode('utf-8','ignore')
        sel = Selector(response)
        infos = sel.xpath('//div[@class="left-col"]//div[@class="f"]/a/@href').extract()
       
        for i in infos:
            print "this is ---->",i
            yield Request(i, callback=self.parse_listing)

        #next = sel.xpath('//div[@class="left-col"]/div[@class="p"]/a/@href').extract()
        #for i in next:
        #    url_i = "http://%s/%s" % (urlparse.urlparse(response.url).hostname, i)
        #    print "========", url_i
        #    yield Request(url_i, callback=self.parse)
    

    def parse_listing(self, response):
        print "111-------------"
        
        sel = Selector(response)
        item = WebItem()

        #if response.getcode() == 404 :
        #    return

        item['name'] = ''.join(sel.xpath('//div[@id="banner"]//text()').extract())

        if item['name'] == '':
            item['name'] = ''.join(sel.xpath('//span[@id="lblCompanyName"]//text()').extract())

        infos = sel.xpath('//div[@id="lianxi-whole"]//div[@id="lianxi-text"]//text()').extract()
        
        for i in infos:
            if "Email" in i:
                item['email'] = i
                print i
       
        if item['email'] == '':
            item['email'] = ''.join(sel.xpath('//span[@id="lblEmail"]//text()').extract())

       
        return item
