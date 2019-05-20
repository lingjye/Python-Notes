#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
import queue
import threading
import multiprocessing

from multiprocessing import Pool
import time
from itertools import groupby

def request(item, item2):
	time.sleep(3)
	print(item, item2)

def run_monitor():

	while True:
		pool = Pool(10)

		list = [str(x) for x in range(100)]

		# pool.map(request, list)



		for x in list:
			pool.apply_async(request, (x,'你好',))

		pool.close()
		pool.join()
		print('结束')

		time.sleep(10)

run_monitor()
