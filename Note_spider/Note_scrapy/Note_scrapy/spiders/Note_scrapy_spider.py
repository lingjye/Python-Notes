# -*- coding: utf-8 -*-
import scrapy


class NoteScrapySpiderSpider(scrapy.Spider):
    name = 'Note_scrapy_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
