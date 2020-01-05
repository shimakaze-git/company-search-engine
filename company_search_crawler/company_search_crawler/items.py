# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanySearchCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CrawlCompany(scrapy.Item):
    url = scrapy.Field()


class Company(scrapy.Item):
    name = scrapy.Field()
    name_kana = scrapy.Field()
    corporate_name = scrapy.Field()
    foundation_date = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
