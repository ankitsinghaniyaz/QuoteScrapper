# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    qid = scrapy.Field()
    quote = scrapy.Field()
    author = scrapy.Field()
    source = scrapy.Field()
