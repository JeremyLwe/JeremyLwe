# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagoucrawlItem(scrapy.Item):

    companyFullName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    education = scrapy.Field()
    industryField = scrapy.Field()
    positionId = scrapy.Field()
    positionName = scrapy.Field()
    workYear = scrapy.Field()
    city = scrapy.Field()