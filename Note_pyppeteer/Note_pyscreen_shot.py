#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
from pyppeteer import launch
import logging

js_str = """
() => {
   return {
       width: document.body.parentNode.scrollWidth,
       height: document.documentElement.scrollHeight,
       deviceScaleFactor: window.devicePixelRatio,
   }
}
"""

class ASyncScreenShot:
    def __init__(self, url, save_path):
        self.url = url
        self.save_path = save_path


    async def run(self):
        print('截图', self.save_path, self.url)
        # lanch(executablePath='your chrome path') 指定chrome路径
        browser = await launch()
        try:
            page = await browser.newPage()
            await page.goto(self.url, options={'timeout':100000})

            dimensions = await page.evaluate(js_str)

            print(dimensions)
            width = int(dimensions["width"])
            height = int(dimensions["height"])

            await page.setViewport({"width": width, "height": height})
            await page.screenshot({"path": self.save_path})

        except Exception as e:
            logging.exception(e)

        await browser.close()

    # 协程 使用async with ASyncScreenShot() as shot 时必须实现的方法
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('退出')

import asyncio
import datetime
screen_shot = ASyncScreenShot("http://www.baidu.com/", "example.jpg")

start_time = datetime.datetime.now()
print('开始:', start_time)
asyncio.get_event_loop().run_until_complete(screen_shot.run())
print('耗时:', datetime.datetime.now()-start_time)