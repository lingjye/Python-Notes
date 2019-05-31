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

# import asyncio
# import time
# import threading
#
# from concurrent.futures import ThreadPoolExecutor
#
# e = ThreadPoolExecutor()
#
#
# def worker(index):
#     print(index, 'before:', time.time())
#     time.sleep(1)
#     print(index, 'after:', time.time())
#     return index
#
#
# def main(index):
#     loop = asyncio.new_event_loop()
#     rv = loop.run_until_complete(loop.run_in_executor(e, worker, index))
#     print('Thread', index, 'got result', rv)
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=main, args=(i,))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

# 解决协程IO阻塞
import asyncio
import time, threading
from multiprocessing.dummy import Pool

async_pool = Pool(200) # 控制200个并发

#需要执行的耗时异步任务
async def func(num):
    print(f'准备调用func,大约耗时{num}')
    await asyncio.sleep(num)
    print(f'耗时{num}之后,func函数运行结束')

#定义一个专门创建事件循环loop的函数，在另一个线程中启动它
def start_loop(loop, cor):
    asyncio.set_event_loop(loop)
    # loop.run_forever()
    loop.run_until_complete(asyncio.wait([cor]))

async def request(id, q):
    while not q.empty():
        i = await q.get()
        # print(i, id)
        try:
            loop(i)
        except asyncio.TimeoutError as e:
            print('错误', e)

def loop(i):
    coroutine1 = start_request(i)

    new_loop = asyncio.new_event_loop()  # 在当前线程下创建时间循环，（未启用），在start_loop里面启动它
    # t = threading.Thread(target=start_loop, args=(new_loop, coroutine1))  # 通过当前线程开启新的线程去启动事件循环
    # t.start()
    # asyncio.set_event_loop(new_loop)
    # new_loop.run_until_complete(asyncio.wait([coroutine1]))

    result = async_pool.map_async(start_request, (new_loop, coroutine1))
    result.wait()
    async_pool.apply_async(start_loop, (new_loop, coroutine1))

    asyncio.run_coroutine_threadsafe(coroutine1, new_loop)  # 这几个是关键，代表在新线程中事件循环不断“游走”执行

async def start_request(i):
    print(i)
    time.sleep(1)

#定义一个main函数
def main():
    q = asyncio.Queue()

    [q.put_nowait(item) for item in range(1000)]
    loop = asyncio.get_event_loop()
    tasks = [request(task_id, q, ) for task_id in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))

    # coroutine1 = func(1)
    # coroutine2 = func(2)
    # coroutine3 = func(3)

    # new_loop = asyncio.new_event_loop()  # 在当前线程下创建时间循环，（未启用），在start_loop里面启动它
    # t = threading.Thread(target=start_loop, args=(new_loop,i))  # 通过当前线程开启新的线程去启动事件循环
    # t.start()
    #
    # asyncio.run_coroutine_threadsafe(coroutine1, new_loop)  # 这几个是关键，代表在新线程中事件循环不断“游走”执行
    # asyncio.run_coroutine_threadsafe(coroutine2, new_loop)
    # asyncio.run_coroutine_threadsafe(coroutine3, new_loop)
    #
    # for i in "iloveu":
    #     print(str(i) + "    ")

    print('结束')

if __name__ == "__main__":
    main()


'''运行结果为：
i    准备调用func,大约耗时3
l    准备调用func,大约耗时2
o    准备调用func,大约耗时1
v
e
u
耗时1之后,func函数运行结束
耗时2之后,func函数运行结束
耗时3之后,func函数运行结束
'''
