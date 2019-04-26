#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import re

test_date = '他的生日是2016-1-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.2016/12/25, .11:39, 12:39:59.223'

test_datetime = '他的生日是2016-12-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.11:34'

# 提取时间
mat = re.findall(r"\d{4}[./-]\d{1,2}[./-]\d{1,2}|\d{2}:\d{2}:\d{2}|\d{2}:\d{2}", test_date)
print(mat)

# 提取html元素
url = '''
<a target="_blank" href="http://www.79.com/ganxi/yizhilian/">
					<img height="118" width="120" border="0" alt="干洗加盟" src="http://img.79.com/TJW/201709/b501b37ccef46d62edf7f69fde3b6f7e4164.jpg">
					<p><i class="xy0"></i>衣之恋干洗加盟</p>衣之恋干洗加盟</a>
'''
r = r'href=\"(http://www.79.com/[a-z]+/[a-z]+/)\"[\s\S]+alt=\"(.*?)\"[\s\S]+src=\"(.*?)\"[\s\S]+$'
print(re.findall(r, url))
print(re.findall(r'href="http://www.79.com/[a-z]+/[a-z]+/', url))
print(re.findall(r'[\s\S]+alt="(.*?)"', url))
print(re.findall(r'[\s\S]+src="(.*?)"[\s\S]+$', url))

r = r''

if r:
	print('1')
else:
	print('2')

url = 'http://www.79.com/sdafsa/fdsaf/'
href_prefix = 'http://www.79.com'
regx = r'%s/[a-z]+/[a-z]+/$' % (href_prefix)
print(regx)
find = re.findall(regx, url)
print(len(find))
if len(re.findall(regx, url)) > 0:
	print('find')

if not 'www.78.com' in url:
	print('find')

url = 'http://www.79.com/sdafsa/123/'
regx = r'%s/[a-z]+/[0-9]+/$' % (href_prefix)
find = re.findall(regx, url)
print(find)

url = 'http://www.79.com/sdafsa/sadasd'
regx = r'%s/[a-z]+/[a-z]+$' % (href_prefix)
find = re.findall(regx, url)
print(find)