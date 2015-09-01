# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import re

class WebPipeline(object):

    def open_spider(self, spider):
        self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
        self.file.write('name,food,openings\n')
        
    def process_item(self, item, spider):
        self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['food'].encode('utf-8')))
        self.file.write('"%s"\n' % (item['openings'].encode('utf-8')))
        
        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()
