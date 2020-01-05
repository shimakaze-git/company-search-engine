# -*- coding: utf-8 -*-
import scrapy
from company_search_crawler.items import CrawlCompany

from typing import List


class ScrapyCompanySearchSpiderSpider(scrapy.Spider):
    name = "scrapy_company_search_spider"
    # allowed_domains = ["omotenashi.site/company"]
    allowed_domains = ["omotenashi.site"]
    start_urls = ["https://omotenashi.site/company/"]

    # page_countr
    page_count = 340

    def parse(self, response):

        scray_prefectures = ["tokyo"]

        start_url = self.start_urls[0]
        if start_url == response.url:
            contents = response.css("#contents")
            groups = contents.css(".bgOriginalCat01 .groupLink01")
            ul_tag = groups.css("dd ul")

            for post in ul_tag.css("li"):
                url = post.css("a::attr(href)").extract_first().strip()

                prefecture = url.replace("/company/", "").replace("/", "")
                if prefecture in scray_prefectures:
                    older_post_link = response.urljoin(url)
                    yield scrapy.Request(older_post_link, callback=self.parse)
        else:
            company_list = self.get_crawl_list(response)
            for company in company_list:
                yield CrawlCompany(url=company["url"])

            # 次のページをのリクエストを実行する
            yield self.next_page_link(response)

    def next_page_link(
        self, response: scrapy.http.response.html.HtmlResponse
    ) -> scrapy.Request:
        """
        次のクローリング先のURLを生成し、scray.Requestオブジェクトを生成する.

        Args:
            response (scrapy.http.response.html.HtmlResponse): オブジェクト.

        Returns:
            scrapy.Request: scrapy.Requestオブジェクトを返す.
        """

        self.page_count += 1

        # index path
        index_path = "index_" + str(self.page_count) + ".html"
        index_path = index_path if self.page_count != 1 else ""

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(index_path)

        # 次のページをのリクエストを実行する
        return scrapy.Request(older_post_link, callback=self.parse)

    def get_crawl_list(self, response: scrapy.http.response.html.HtmlResponse) -> List:
        """
        DOMの内容から企業情報が載っているURlを取得する.

        Args:
            response (scrapy.http.response.html.HtmlResponse): オブジェクト

        Returns:
            List: 企業の情報が入ったListを返す.
        """
        company_list = []

        company_list_box = response.css(".entryList01")
        company_list_tag = company_list_box.css("li")

        for company in company_list_tag:
            company_path = company.css("a::attr(href)").extract_first()
            company_url = response.urljoin(company_path)

            company_list.append({"url": company_url})

        return company_list
