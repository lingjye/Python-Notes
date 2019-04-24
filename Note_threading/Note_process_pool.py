#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

from multiprocessing import Pool, Process
import time

def func(i):
	print(i)
	time.sleep(30)
	print('结束:', i)

if __name__ == '__main__':
	pool = Pool(8)	#设定进程数
	s_time = time.time()
	a = pool.map(func, range(16))
	print(a)

	e_time = time.time()
	print(e_time - s_time)
