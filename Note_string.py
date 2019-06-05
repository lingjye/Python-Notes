#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import re
# 分割
s1 = 'adnm|sdjka|sa|123'
s2 = 'wqewq'
print(s1.split('|'))
print(s2.split('|'))

# 通过字符集分割
r1 = re.split('[a|s]', s1)
print(r1)

request_url = 'https://www.baidu.com/'

if request_url[len(request_url) - 1] == '/':
	href_prefix = request_url[:len(request_url) - 1]
else:
	href_prefix = request_url

print(href_prefix)

# 去除空格
s3 = ' sfdasf '
print(s3)
print(s3.strip())
print(s3)

s4 = 'http://sfdasf/'
print(s4)
print(s4.strip('/'))
print(s4)

bstr = b'www'
test_str = b'www.baidu.com'
print(test_str.find(bstr) != -1)


url = 'http://sjh.baidu.com'
print(url.startswith('http://sjh.baidu.com'))
