# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field()
    ratevalue = scrapy.Field()
    reviewcount = scrapy.Field()
    address = scrapy.Field()
    postcode = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    telephone = scrapy.Field()
    website = scrapy.Field()
    price = scrapy.Field()
    #pass
