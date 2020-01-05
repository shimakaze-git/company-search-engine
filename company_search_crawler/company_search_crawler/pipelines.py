# -*- coding: utf-8 -*-

from company_search_crawler.spiders import scrapy_company_search_spider
from company_search_crawler.repositories import ScrapyCompanySearchRepository

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CompanySearchCrawlerPipeline(object):
    def __init__(self):
        super().__init__()

        self.save_repository = None

    def open_spider(self, spider):
        """
        保存処理などを行うリポジトリを選択する.

        :param spider: ScrapyのSpiderオブジェクト
        """

        spider_name = str(scrapy_company_search_spider.__name__.split(".")[2])
        if spider_name == str(spider.name):
            self.save_repository = ScrapyCompanySearchRepository()

    def process_item(self, item, spider):
        """ プロセス処理. """

        self.save_repository.execute(item)
        return item

    def close_spider(self, spider):
        """
        終了処理.
        csvに保存する.

        :param spider: ScrapyのSpiderオブジェクト
        """

        self.save_repository.save()
