# -*-coding:utf-8-*-
import scrapy


class QuotesSpider(scrapy.Spider):
    """抓取名人名言的爬虫"""
    name = "quotes"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',  # 只搜索分类
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
