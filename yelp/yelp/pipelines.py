# -*- coding: utf-8 -*-
import time

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YelpPipeline(object):
        
    def open_spider(self, spider):
        self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
        self.file.write('Head Title\n')
        
    def process_item(self, item, spider):
        #self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['name']))
        self.file.write('"%s",' % (item['ratevalue']))
        self.file.write('"%s",' % (item['reviewcount']))
        self.file.write('"%s",' % (item['streetaddr']))
        self.file.write('"%s",' % (item['postcode']))
        self.file.write('"%s",' % (item['addrlocality']))
        self.file.write('"%s",' % (item['telephone']))
        self.file.write('"%s\n"' % (item['price']))
        
        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()

        
