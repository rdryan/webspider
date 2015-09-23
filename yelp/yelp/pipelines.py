# -*- coding: utf-8 -*-
import time
##################################################
# rdryan@sina.com
# Copyright (c) 2015
##################################################

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YelpPipeline(object):
        
    def open_spider(self, spider):
        self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
        self.file.write('name,category,ratevalue,reviewcount,address,postcode,city,area,telephone,website,price\n')
        
    def process_item(self, item, spider):
        #self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['category'].encode('utf-8')))
        self.file.write('"%s",' % (item['ratevalue']))
        self.file.write('"%s",' % (item['reviewcount']))
        self.file.write('"%s",' % (item['address'].encode('utf-8')))
        self.file.write('"%s",' % (item['postcode']))
        self.file.write('"%s",' % (item['city'].encode('utf-8')))
        self.file.write('"%s",' % (item['area'].encode('utf-8')))
        self.file.write('"%s",' % (item['telephone']))
        self.file.write('"%s",' % (item['website']))
        self.file.write('"%s",' % (item['price'].encode('utf-8')))
        self.file.write('"%s"\n' % (item['url']))
        
        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()

        
