# -*- coding: utf-8 -*-
import time
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RealestatePipeline(object):

    def open_spider(self, spider):
        self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
        self.file.write('name,price,url\n')

    def process_item(self, item, spider):
        self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['price'].encode('utf-8')))
        self.file.write('"%s"\n' % (item['url'].encode('utf-8')))

        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()

