#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
'''
信号量
'''

'''
import threading

import time

sem = threading.Semaphore(3) #限制线程的最大数量4个

def limitBySepmaphore():
	for i in range(10):
		threading.Thread(target=gothread).start()

def gothread():
	# 锁定线程的最大数量
	with sem:
		for i in  range(8):
			print(threading.current_thread().name, i)
			time.sleep(1)
'''

'''
自定义线程池
'''
'''
class scanner(threading.Thread):

	tlist = []	#用来存储队列的线程
	maxthread = 10 # int(sys.argv[2])最大的并发数量，此处我设置为100，测试下系统最大支持1000多个
	evnt = threading.Event()	##用事件来让超过最大线程设置的并发程序等待
	lck = threading.Lock()	#线程锁

	def __init__(self, counter):
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self):
		try:
			print(self.name)
			self.request()
		except Exception as e:
			print(e)

		# 以下用来将完成的线程移除线程队列
		scanner.lck.acquire()
		scanner.tlist.remove(self)

		#如果移除此完成的队列线程数刚好达到99, 则说明有线程在等待执行, 那么我们释放event,让等待时间执行
		if len(scanner.tlist) == scanner.maxthread - 1:
			scanner.evnt.set()
			scanner.evnt.clear()

		scanner.lck.release()

	def request(self):
		time.sleep(1)
		# headers = {'User-Agent': random.choice(USER_AGENTS_LIST)}
		# print(headers)
		# page = request.Request('http://baidu.shgao.com/jiameng/kongqvezaixian/', headers=headers)
		# page_info = request.urlopen(page).read()
		# hash_code = hashlib.md5(page_info)
		# print(hash_code, self.name)

	def newthread(counten):
		scanner.lck.acquire()	#上锁
		sc = scanner(counten)
		scanner.tlist.append(sc)
		scanner.lck.release()	#解锁
		sc.start()

	#将新线程方法定义为静态变量, 供调用
	newthread = staticmethod(newthread)

def runnscan():
	while True:
		for i in range(100):
			scanner.lck.acquire()
			#如果目前线程队列超过了设定的额上限则等待
			if len(scanner.tlist) >= scanner.maxthread:
				scanner.lck.release()
				scanner.evnt.wait()	#scanner.evnt.set()遇到set事件则等待结束
			else:
				scanner.lck.release()
			scanner.newthread(i)

		for t in scanner.tlist:
			# join的操作使得后面的程序等待线程的执行完成才能继续
			t.join()

		while threading.active_count() != 0:
			if threading.active_count() == 1:
				print('结束')
				time.sleep(6)
				break

if __name__ == '__main__':
    # limitBySepmaphore()
	runnscan()
'''