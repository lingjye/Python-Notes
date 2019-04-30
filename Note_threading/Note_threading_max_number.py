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


import threading
import random
import queue
from time import sleep
import sys
#
#需求分析：有大批量数据需要执行，而且是重复一个函数操作（例如爆破密码），如果全部开始线程数N多，这里控制住线程数m个并行执行，其他等待
#
#继承一个Thread类，在run方法中进行需要重复的单个函数操作
class Test(threading.Thread):
  def __init__(self,queue,lock,num):
    #传递一个队列queue和线程锁，并行数
    threading.Thread.__init__(self)
    self.queue=queue
    self.lock=lock
    self.num=num
  def run(self):
    #while True:#不使用threading.Semaphore，直接开始所有线程，程序执行完毕线程都还不死，最后的print threading.enumerate()可以看出
    with self.num:#同时并行指定的线程数量，执行完毕一个则死掉一个线程
      #以下为需要重复的单次函数操作
      n=self.queue.get()#等待队列进入
      lock.acquire()#锁住线程，防止同时输出造成混乱
      print('开始一个线程：',self.name,'模拟的执行时间：',n)
      print('队列剩余：',queue.qsize())
      print(threading.enumerate())
      lock.release()
      sleep(3)#执行单次操作，这里sleep模拟执行过程
      self.queue.task_done()#发出此队列完成信号
threads=[]
queue=queue.Queue()
lock=threading.Lock()
num=threading.Semaphore(3)#设置同时执行的线程数为3，其他等待执行
#启动所有线程
for i in range(10):#总共需要执行的次数
  t=Test(queue,lock,num)
  t.start()
  threads.append(t)
  #吧队列传入线程，是run结束等待开始执行，放下面单独一个for也行，这里少个循环吧
  n=random.randint(1,10)
  queue.put(n)#模拟执行函数的逐个不同输入
#吧队列传入线程，是run结束等待开始执行
# for t in threads:
#  n=random.randint(1,10)
#  queue.put(n)
#等待线程执行完毕
for t in threads:
  t.join()
queue.join()#等待队列执行完毕才继续执行，否则下面语句会在线程未接受就开始执行
print('所有执行完毕')
print(threading.active_count())
print(threading.enumerate())

import time

def my_print(index):
  print('开始', index)
  time.sleep(1)
  print('结束:', index)

thread1 = threading.Thread('name1', my_print(1))
thread2 = threading.Thread('name2', my_print(2))
thread1.start()
thread1.join()
thread2.start()
thread2.join()
