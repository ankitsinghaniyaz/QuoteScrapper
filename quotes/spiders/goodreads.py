# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from quotes.items import QuotesItem
from scrapy.http.request import Request
from scrapy.spiders import Rule


class GoodreadsSpider(scrapy.Spider):
    name = "goodreads"
    allowed_domains = ["www.goodreads.com"]
    start_urls = ("https://www.goodreads.com/quotes",)
    rules = (Rule(LinkExtractor(deny=('')))) # do not crawl any link on page

    def parse(self, response):
        # get div with quote and author
        quotes = response.xpath('//div[@class="quoteText"]')
        for quote in quotes:
            try:
                item = QuotesItem()
                item['quote'] = quote.xpath('text()').extract_first().strip()[1:-1]
                item['author'] = quote.xpath('a/text()').extract_first().strip().split(',')[0]
                item['source'] = self.name
                yield item
            except:
                pass
        # find the next page link and go
        next_page = response.xpath('//a[@class="next_page"]/@href').extract_first()
        yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
