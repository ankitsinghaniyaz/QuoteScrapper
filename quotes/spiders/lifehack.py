# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.spiders import Rule


class LifehackSpider(scrapy.Spider):
    name = "lifehack"
    allowed_domains = ["quotes.lifehack.org", "lifehack.org"]
    rules = (Rule(LinkExtractor(deny=(''))))
    # x = response.xpath('//li[@data-quote-id]').extract_first()
    # x = response.xpath('//li[@data-quote-id]/h4/text()').extract_first()
    # x = response.css('li').xpath('@data-quote-id').extract()
    # x = response.xpath('//li/@data-quote-id')[0].extract()
        # http://pythonscraping.com/blog/xpath-and-scrapy
    # start_urls = (
    #     'http://quotes.lifehack.org/quote/p/255794/'
    # )

    # This function is overidden to create start urls
    def start_requests(self):
        base_url = "http://quotes.lifehack.org/quote/p/"
        # for i in range(100, 300000):
        for id in range(100, 300000):
            url = base_url + str(id) + '/'
            yield Request(url, self.parse, meta={'id': id})

    def parse(self, response):
        if response.status == 200:
            print(response)
            print(response.meta['id'])
