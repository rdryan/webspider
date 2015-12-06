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

    driver = webdriver.PhantomJS()
    

    def parse(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)

        print self.driver.page_source

        
        articles = sel.xpath('//article[contains(@class,"job-tile")]')

        for article in articles:
            header = ''.join(article.xpath('//header//text()').extract())
            print header

        print "this is a test===="
        pass
