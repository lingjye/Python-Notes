#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import aiohttp
import asyncio
import logging
import datetime

MaxTasks = 500

def start_request(items):
	# 创建asyncio队列
	q = asyncio.Queue()
	# 设置url到队列中
	[q.put_nowait(url) for url in items]
	# 获取当前事件循环
	loop = asyncio.get_event_loop()
	# 设置队列最大并发
	tasks = [request(task_id, q,) for task_id in range(MaxTasks)]
	# 运行,直到所有任务结束, 超时时间3600s
	loop.run_until_complete(asyncio.wait(tasks, timeout=3600))
	# 关闭当前loop
	loop.close()

async def request(task_id, request_queue):
	while not request_queue.empty():
		current_url = await request_queue.get()
		try:
			# 协程等待
			await request_item(current_url)
		except Exception as e:
			logging.exception(e)
# 协程 异步
async def request_item(url):
	html, http_status = await parse_body(url)
	print('结果:', http_status, len(html));

# 解析数据, 失败后重试两次
async def parse_body(url, retries_num=2):
	async with aiohttp.ClientSession() as session:
		status = 0
		try:
			async with session.get(str(url)) as response:
				status = response.status
				response.raise_for_status()
				html = await response.read()
				return html, status
		except asyncio.TimeoutError as e:
			# 超时
			if retries_num > 0:
				return await parse_body(url, retries_num-1)
			logging.exception(e)
		except Exception as e:
			logging.exception(e)

		return b'', status

def urllib3_pool(items):
	pool = urllib3_pool()

if __name__ == '__main__':
	start_time = datetime.datetime.now()
	items = ['https://www.baidu.com' for _ in range(5000)]
	print(items)
	start_request(items)
	# 测试 21s 左右
	print('耗时:', datetime.datetime.now()-start_time)