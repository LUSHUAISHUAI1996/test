# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    """抓取名言"""
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attrls("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_tag(self, response):
        pass
