#!/usr/bin/env python
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint

class HttpDupeFilter(BaseDupeFilter):
	def __init__(self):
		#初始化visited_fd为一个集合[也可以放到redis中]
		self.visited_fd = set()

	@classmethod
	def from_settings(cls, settings):
		return cls()

	def request_seen(self, request):
		'''
		:param request: 请求url[进行类似md5加密的操作]
		http://www.baidu.com?su=123&456
		http://www.baidu.com?su=456&123 以上两个的伪MD5是一样的
		伪MD5值得方法是request_fingerprint
		:return:
		'''
		print('=======过滤=======')
		# print(request, type(request))
		try:
			item = request.meta['item']
			title = item['title']
		except:
			title = None
		# print(item)
		#如果href和title一样, 则过滤请求
		# if not title:
		# 	fd = request_fingerprint(request=request)
		# else:
		fd = request_fingerprint(request=request)
		# 如果路径在visited_fd中返回True
		if fd in self.visited_fd:
			print('已过滤:', request)
			return True
		#添加到集合中
		self.visited_fd.add(fd)

	def open(self):	#can return deferred
		print('=====开始=====')

	def close(self, reason):	#can return a deferred
		print('=====结束=====')

	def log(self, request, spider):	#log that a request has been filterd
		print('=====日志=====')
		spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)

