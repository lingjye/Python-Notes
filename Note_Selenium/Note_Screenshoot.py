#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

'''
pip install pillow
pip install selenium
'''

from selenium import webdriver
import os
import time

from selenium import webdriver
import os
import hashlib
# from PIL import Image
import sys
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.wait import WebDriverWait

driverPath = os.path.abspath('driver')
phanJSDriverPath = os.path.join(driverPath, 'phantomjs')
chromDriverPath = os.path.join(driverPath, 'chromedriver')
geckoDriverPath = os.path.join(driverPath, 'geckodriver')
print(chromDriverPath, phanJSDriverPath, geckoDriverPath)

screen_shots_path = os.path.abspath('screen_shots')
print(screen_shots_path)

'''
Chrome 智能截取当前窗口内容
'''
chrome_options = webdriver.ChromeOptions()
# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('--headless')
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# 隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('--hide-scrollbars')
# 最大化
# chrome_options.add_argument('--start-maximized');
# 全屏
# chrome_options.add_argument('--start-fullscreen');

#不加载图片, 提升速度
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# 注意:使用Chrome只能截取当前窗口的内容, PhantomJS可截取整个内容
browser = webdriver.Chrome(chromDriverPath, chrome_options=chrome_options)

# gecko_options = Options()
# gecko_options.add_argument('--headless')
# gecko_options.add_argument('--start-maximized')
# gecko_options.add_argument('--start-fullscreen')
# gecko_options.add_argument('--disable-gpu')
# browser = webdriver.Firefox(executable_path=geckoDriverPath, options=gecko_options)

# browser = webdriver.PhantomJS(phanJSDriverPath)

# wait = WebDriverWait(browser, 20)

# 设置超时 下边两种设置都进行才有效
browser.set_page_load_timeout(20)
# 设置异步脚本超时时间
browser.set_script_timeout(20)

# url = 'http://bdwap.818489.com/shbfsqgpp12/'
url = 'http://9.txooo.com/brands/496539/Default.html'
browser.get(url)

page_info = browser.page_source

print(type(page_info))
# soup = BeautifulSoup(page_info, 'html.parser')
# page_info = str(soup)
# metas = soup.find_all('meta')
# #去除meta标签中的时间变化
# for meta in metas:
# 	meta_str = str(meta)
# 	# print(meta_str)
# 	mat = re.findall(r"\d{4}[./-]\d{1,2}[./-]\d{1,2}|\d{2}:\d{2}:\d{2}|\d{2}:\d{2}", meta_str)
# 	# print(mat)
# 	if len(mat):
# 		print('替换', meta_str)
# 		page_info = page_info.replace(meta_str, '<meta/>')

js_height = "return document.body.clientHeight"
k = 1
height = browser.execute_script(js_height)
while True:
	if k * 500 < height:
		js_move = "window.scrollTo(0,{})".format(k * 500)
		print(js_move)
		browser.execute_script(js_move)
		time.sleep(0.2)
		height = browser.execute_script(js_height)
		k += 1
	else:
		break
scroll_width = browser.execute_script(
	'return document.body.parentNode.scrollWidth')
scroll_height = browser.execute_script(
	'return document.body.parentNode.scrollHeight')
browser.set_window_size(scroll_width, scroll_height)
current_time = time.strftime("%Y%m%d%H%M%S",
							 time.localtime(time.time()))
imageFullName =  os.path.join(screen_shots_path, 'test.img')
print(imageFullName)
browser.get_screenshot_as_file(imageFullName)
print("Process {} get one pic {}!!!".format(os.getpid(),
											imageFullName))
time.sleep(0.1)

#
# hashCode = hashlib.md5(page_info.encode('utf-8')).hexdigest().upper()
#
# print(hashCode)
# # print(page_info)
#
# # time.sleep(5)
#
# page_info = browser.page_source
#
# hashCode = hashlib.md5(page_info.encode('utf-8')).hexdigest().upper()
#
# print(hashCode)
# # print(page_info)
#
#
# picName = hashlib.md5(url.encode('utf-8')).hexdigest() + '.png'
# picWebPName = hashlib.md5(url.encode('utf-8')).hexdigest() + '.webp'
# picPath = os.path.join(screen_shots_path, picName)
# picWebPPath = os.path.join(screen_shots_path, picWebPName)
#
# # 保存截图到本地
# # browser.save_screenshot(picPath)
# # 此处不直接保存 先转化为webp格式图片再保存
# imgBuf = browser.get_screenshot_as_png()
#
# f = BytesIO(imgBuf)
#
# img_webp = Image.open(f)
#
# size_bs = sys.getsizeof(img_webp)
# print('内容占用内存:', str(size_bs))
#
# img_webp.save(picWebPPath)
#
# elements = browser.find_elements_by_class_name('f1_left')
# if len(elements):
# 	print(elements, len(elements))
# 	element = elements[0]
# 	print(element)
#
# 	left = element.location['x']
# 	top = element.location['y']
# 	right = element.location['x'] + element.size['width']
# 	bottom = element.location['y'] + element.size['height']
#
# 	# 截取元素内容
# 	resultImg = Image.open(picWebPPath)
# 	resultImg = resultImg.crop((left, top, right, bottom))
# 	resultImg.save(os.path.join(screen_shots_path, 'crop_result' + picWebPName), 'WEBP');

browser.quit()