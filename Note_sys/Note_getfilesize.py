#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import os
import sys

# 获取本地文件大小 字节B 与实际相符
ca_size = os.path.getsize('README.md')
print(ca_size)

s = ''

with open('README.md', 'r') as f:
	s += f.read()

print(s)

# 对象内存跟文件内存不一致, 详见 Note_sys.py 对象占用空间获取
s_size = sys.getsizeof(s)
print(s_size)

