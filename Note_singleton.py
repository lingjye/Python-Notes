#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import datetime
import time
import gc

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class Highlander(object):
    # x = 100
    # Of course you can have any attributes or methods you like.
	def __init__(self):
		print('创建')
		self.config_params()

	def config_params(self):
		self.x = 100
		self.date = datetime.datetime.now()

	def __call__(self, *args, **kwargs):
		print('调用')

	def get_value(self, input):
		return 200 + input

	def __del__(self):
		print('__del__')
		self.x = None
		self.date = None

print(Highlander.date, Highlander)

print('休眠')
time.sleep(3)
print(Highlander.date)
print('休眠结束')

print('删除')

Highlander.config_params()

print(Highlander.date)




