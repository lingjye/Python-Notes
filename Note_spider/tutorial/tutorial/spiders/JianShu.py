# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import TutorialItem

class JianshuSpider(scrapy.Spider):
    name = 'JianShu'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    # 重写父类的方法, 处理 start_urls 参数等
    def start_requests(self):
        yield Request('http://www.jianshu.com/',
                      callback=self.parse,
                      meta={"item": 'item'},
                      dont_filter=False,
                      )


    def parse(self, response):
        meta = response.meta['item']
        print(meta, response.body)
        items = []
        item = TutorialItem()
        item.title = ''
        item.author = ''
        item.img = ''
        item.url = ''
        for item in items:
            yield Request(item.url,
                          callback=self.parse_content,
                          meta={"item": 'item'},
                          dont_filter=False,
                          )

        return items

    def parse_content(self, response):
        meta = response.meta['item']
        print(meta, response.body)
        pass
