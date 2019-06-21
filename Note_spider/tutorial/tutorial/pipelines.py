# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class TutorialPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        # self.file = codecs.open('item.json', 'wb', encoding='utf-8')
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
        scrapy为我们访问settings提供了这样的一个方法，这里，
        我们需要从settings.py文件中，取得数据库的URI和数据库名称
        '''
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB'),
        )

    def open_spider(self, spider):
        '''
        爬虫一旦开启, 就会实现这个方法, 链接到数据库
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        '''
        爬虫一旦关闭，就会实现这个方法，关闭数据库连接
        '''
        self.client.close()

    def process_item(self, item, spider):
        '''
        每个实现保存的类里面必须要有这个方法, 且名字固定, 用来具体实现怎么保存
        '''
        # if not item['title']:
        #     # return item
        #     print('item不存在title:',item)
        '''
        SQLServer 更新数据库
        '''
        if not item['description']:
            return item

        '''
        MongoDB 更新数据库 
        '''
        # 本地测试 MongoDB
        data = {
            'title': item['title'],
            'author': item['author'],
            'img': item['img'],
            'url': item['url'],
        }
        #
        table = self.db[spider.name]
        # # table.insert_one(data)
        table.update({'href': item['href']}, data, True);
        return item