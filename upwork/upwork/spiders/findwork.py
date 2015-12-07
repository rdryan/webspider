# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from upwork.items import UpworkItem
from selenium import webdriver


class FindworkSpider(scrapy.Spider):
    name = "findwork"
    allowed_domains = ["upwork.com"]
    start_urls = (
        #'http://www.upwork.com/',
        'https://www.upwork.com/o/jobs/browse/?q=python',
    )

    service_args = [
        '--ignore-ssl-errors=true',
        #'--ssl-protocol=TLSv1',
    ]
    driver = webdriver.PhantomJS(service_args=service_args)
    #driver = webdriver.Chrome()
    

    def parse(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)

        #print self.driver.page_source

        articles = sel.xpath('//article[contains(@class,"job-tile")]')
        item = UpworkItem()
        
        for article in articles:
            header = ''.join(article.xpath('//header//text()').extract())
            
            item['jobtitle'] = header.strip()

        
        yield item

        self.driver.quit()
        #pass
