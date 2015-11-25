# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    content = scrapy.Field()
    phone_num = scrapy.Field()
    email = scrapy.Field()

    image_url = scrapy.Field()
    
    pass
