#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

# 分割
s1 = 'adnm|sdjka|sa|123'
s2 = 'wqewq'
print(s1.split('|'))
print(s2.split('|'))

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