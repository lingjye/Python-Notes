### Scrapy 笔记

#### 使用Scrapy开启一个爬虫任务
1. 安装:

> pip install scrapy

前往需要放置的路径下

> cd 你的爬虫项目路径

开启一个scrapy项目

> scrapy startproject SrapyProject(你的爬虫项目名称)

创建一个爬虫, 可创建多个

> scrapy genspider ScrapySpider(你的爬虫名字)

运行一个爬虫

> scrapy crawl ScrapySpider(爬虫名字)

