# -*- coding: utf-8 -*-
import scrapy


class ScrapyCompanySpider(scrapy.Spider):
    name = 'scrapy_company'
    allowed_domains = ['omotenashi.site/company']
    start_urls = ['http://omotenashi.site/company/']

    def parse(self, response):
        pass
