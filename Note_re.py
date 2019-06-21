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

url = 'http://www.79.com/web/Sdafsa/sadasd/index.html,' \
	  'http://www.79.com/pro/sdaf_sa/sadasd/index.html,' \
	  'http://www.79.com/sdafsa/sadasd/index.html,' \
	  'http://www.79.com/sdafsa/sadasd' \
	  'http://www.79.com/sdafsa/index.html'
regx = r'%s/web/[a-z]+/[a-z]+/index.html|%s/pro/[a-z]+/[a-z]+/index.html' % (href_prefix, href_prefix)
# 忽略大小写
find = re.findall(regx, url, re.I)
print(find)

regx = r'%s/[web|pro+/[a-z_]+/[a-z]+/index.html' % (href_prefix)
find = re.findall(regx, url, re.I)
print(find)

url = 'my phone is 123-456-567, 132-312, as-312132-312-2131321lk'
regx = r'[0-9]+-?[0-9]+-[0-9]{0,}' # '[0-9]+-?[0-9]+-[0-9]*'
find = re.findall(regx, url)
print(find)

url = 'colou, colour, color, coloara'
regx = r'colo\w?r+\w?'
find = re.findall(regx, url)
print(find)

url = '	匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 、 "does" 中的 "does" 、 "doxzy" 中的 "do" 。? 等价于 {0,1}。'
regx = r'do[es]?\w*'
find = re.findall(regx, url)
print(find)

url = '''
<a target="_blank" href="http://www.79.com/vip/tbh/">
<a target="_blank" href="http://www.79.com/brand/zlfccxc/index/">
<a target="_blank" href="http://www.79.com/brand/zlfccxc/index">
<a target="_blank" href="http://www.79.com/vip/tbh">
<a target="_blank" href="http://www.79.com/vip/tbh/sfdsf">
'''

# 匹配brand/xxxx/xxxx(/) 或者 vip/xxxx/
regx1 = r'%s/brand/[a-z]+/[a-z]+/?|%s/vip/[a-z]+/' % (href_prefix, href_prefix)
# 匹配情况比上班regx1 多一种 vip/xxxx/xxxx(/)
regx2 = r'%s/[brand|vip]+/[a-z][+/[a-z]+]?' % (href_prefix)
find1 = re.findall(regx1, url)
find2 = re.findall(regx2, url)
print(find1)
print(find2)

# 寻找出现两次及以上的单词
str = "Is is the cost of of gasoline going up up up";
patt1 = r'\b([a-z]+) \1\b'
print(re.findall(patt1, str, re.I))

url = '''
<a target="_blank" href="http://www.79.com/brand/zlfccxc/index.htm">
<a target="_blank" href="http://www.79.com/brand/zlfccxc/index.html">
<a target="_blank" href="http://www.79.com/brand/zlfccxc/123123.htm?index=1">
<a target="_blank" href="http://www.79.com/dsad/brand/id/123123.html?index=1">
'''

href_prefix = 'http://www.79.com'

href_regx = r'%s/[a-z]+/[a-z]+/\w+.html?' % (href_prefix)
find1 = re.findall(href_regx, url)
print(find1)

href_regx = r'%s/[a-z]+/brand/id/\d+.html?' % (href_prefix)
find1 = re.findall(href_regx, url)
print(find1)

url = 'http://m.jmw.com.cn/xm6783165/'
href_regx = r'http://m.jmw.com.cn/[a-z]{2}\d+/'
find1 = re.findall(href_regx, url)
print(find1)

url = 'http://m.jmw.com.cn/xm/sdadsa/sdasdsa/, http://m.jmw.com.cn/xm/, http://m.jmw.com.cn/13/13/, http://m.jmw.com.cn/xm/sda/'
href_regx = r"http://m.jmw.com.cn/[a-z]+/?[a-z]+?/"
find1 = re.findall(href_regx, url)
print(find1)
