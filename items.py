# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TimeItem(scrapy.Item):
# define the fields for your item here like:
# name = scrapy.Field()


class policyItem(scrapy.Item):
    title = scrapy.Field()
    articles = scrapy.Field()
    timee = scrapy.Field()
