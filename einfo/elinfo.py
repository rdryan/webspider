# -*- coding: utf-8 -*-
#import scrapy
#from scrapy.selector import Selector
#from scrapy.http import Request

from bs4 import BeautifulSoup
import urlparse
import urllib2
import time

start_urls = (
   #…œ∫£
   #'http://so.cnlinfo.net/gongsi/one_301/pro_440000/1.htm',
   #'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=1',
   'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page=',
   )

url = 'http://search.114chn.com/searchresult.aspx?type=1&key=%E5%B7%A5%E4%B8%9A%E5%85%AC%E5%8F%B8&areaid=31&pattern=2&page='

item = dict()

item['name'] = ''
item['email'] = ''

global file
file = open('output/infos-%s.csv' % (time.strftime("%Y-%m-%d-%H")), 'w+')
file.write('name,email\n')

        
def get_request(url):
    print "request to: ", url
    req = urllib2.Request(url)

    try:
        response = urllib2.urlopen(req, timeout=10)
        return response
    #except urllib2.URLError, e:
    except Exception, e:
        print "XXX Error"
        return False
 
def parse(response):
    if  not response:
        return
    
    html = response.read()
    sel = BeautifulSoup(html)
    #infos = sel.xpath('//div[@class="left-col"]//div[@class="f"]/a/@href').extract()
    infos = sel.findAll('div',attrs={'class':'f'})
   
    for info in infos:
        i = info.find('a')['href']
        response = get_request(i)
        parse_listing(response)


    #next = sel.xpath('//div[@class="left-col"]/div[@class="p"]/a/@href').extract()
    #for i in next:
    #    url_i = "http://%s/%s" % (urlparse.urlparse(response.url).hostname, i)
    #    print "========", url_i
    #    yield Request(url_i, callback=self.parse)


def parse_listing(response):
    if not response:
        return
    
    html = response.read()
    sel = BeautifulSoup(html)

    print "parse_listing -----"
    
    #item['name'] = ''.join(sel.xpath('//div[@id="banner"]//text()').extract())
    names = sel.find('span',attrs={'id':'lblCompanyName'})
    
    if names:
        print names.text
        item['name'] = names.text

    names = sel.find('div',attrs={'id':'banner'})
    if names:
        print names.text
        item['name'] = names.text


    #if item['name'] == '':
    #    item['name'] = ''.join(sel.xpath('//span[@id="lblCompanyName"]//text()').extract())

    #infos = sel.xpath('//div[@id="lianxi-whole"]//div[@id="lianxi-text"]//text()').extract()
    
    #for i in infos:
    #    if "Email" in i:
    #        item['email'] = i
    #        print i
  
    emails = sel.find('span',attrs={'id':'lblEmail'})
    if emails:
        print emails.text
        item['email'] = emails.text
    
    emails = sel.findAll('div',attrs={'id':'lianxi-text'})
    for i in emails:
        if "Email" in i.text:
            print i.text
            item['email'] = i.text
  
    #if item['email'] == '':
    #    item['email'] = ''.join(sel.xpath('//span[@id="lblEmail"]//text()').extract())

    file.write('"%s",' % (item['name'].encode('utf-8')))
    file.write('"%s"\n' % (item['email'].encode('utf-8')))

#######################################################################################
## Main function
#######################################################################################
print "Begin----\n"

#for url in start_urls:
for i in range(1,100):
    print "the number is --", i

    url_i = url + str(i)
    res = get_request(url_i);
    parse(res)

print "End----\n"
file.close()

