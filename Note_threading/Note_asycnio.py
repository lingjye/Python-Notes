#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

# def yield_test(n):
# 	for i in range(n):
# 		yield call(i)
# 		print("i=", i)
# 	# 做一些其它的事情
# 	print("do something.")
# 	print("end.")
#
#
# def call(i):
# 	print( 'yield', i)
# 	return i * 2
#
#
# # 使用for循环
# for i in yield_test(5):
# 	print(i, ",")


# import threading
# import time
#
# def run1():
# 	print('running')
# 	time.sleep(3)
# 	print('当前2:', threading.current_thread().name)
#
# def run(i):
# 	print('run-', i)
# 	print('当前:',  threading.current_thread().name)
# 	time.sleep(1)
# 	t = threading.Thread(target=run1)
# 	t.start()
# 	# t.join()
#
# 	t2 = threading.Thread(target=run1)
# 	t2.start()
# 	# t2.join()
#
# for i in range(5):
# 	t = threading.Thread(target=run, args=(1,))
# # t._target = run
# 	t.start()
# 	t.join()
#
#
# while True:
# 	if threading.active_count() != 1:
# 		pass
# 	else:
# 		print('结束')
# 		break
#
# c = threading.active_count()
# print( '当前1:',  c, threading.current_thread().name)
# print('end')

# import asyncio
# import time

# async def download(url):
# 	print('下载', url)
# 	await asyncio.sleep(3)
# 	print('下载完成')
#
# if __name__ == '__main__':
# 	loop = asyncio.get_event_loop()
# 	urls = [
# 		'https://www.baidu.com',
# 		'http://www.sohu.com',
# 		'http://www.sina.com',
# 		'https://www.taobao.com',
# 		'http://www.qq.com'
# 	]
# 	tasks = [download(url) for url in urls]
# 	loop.run_until_complete(asyncio.wait(tasks))



# import threading
#
#
# def worker():
#     hl = Highlander
#     hl.x += 1
#     print(hl)
#     print(hl.x)
#
#
# def main():
#     threads = []
#     for _ in range(50):
#         t = threading.Thread(target=worker)
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
#
#
# if __name__ == '__main__':
#     main()