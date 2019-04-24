#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
import threading
import time

'''
结果错误 
'''
# class MyThread(threading.Thread):
# 	def run(self):
# 		global num
# 		time.sleep(1)
# 		num += 1
# 		msg = self.name + ' set num to ' + str(num)
# 		print(msg)
#
# num = 0
# def test():
# 	for i in range(5):
# 		t = MyThread()
# 		t.start()
#
# test()


'''
互斥锁同步
'''
# lock = threading.Lock()
# # 锁定
# lock.acquire(1)
# # 释放
# lock.release()

lock = threading.Lock()

class MyThread(threading.Thread):
	def run(self):
		global num
		# time.sleep(1)
		#
		if lock.acquire(1):

			num += 1
			msg = self.name + ' set num to ' + str(num)
			print(msg)
			lock.release()

num = 0

def test():
	for i in range(5):
		t = MyThread()
		t.start()

test()