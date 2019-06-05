#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import urllib3
import datetime
import certifi

def request(items):
	pool = urllib3.PoolManager(timeout=30,
							   num_pools=500,
							   cert_reqs='CERT_REQUIRED',
							   ca_certs=certifi.where()
							   )
	for url in items:
		resp = pool.request('GET', url, retries=10)
		print(resp.status, len(resp.data))


if __name__ == '__main__':
	start_time = datetime.datetime.now()
	items = ['https://www.baidu.com' for _ in range(5000)]
	print(items)

	request(items)
	# 测试 3min50s 左右
	print('耗时:', datetime.datetime.now()-start_time)