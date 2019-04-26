#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import sys

# 以字节（byte）为单位返回对象大小。 这个对象可以是任何类型的对象。
# 所以内置对象都能返回正确的结果 但不保证对第三方扩展有效，因为和具体实现相关。

# getsizeof() 调用对象的 __sizeof__ 方法， 如果对象由垃圾收集器管理， 则会加上额外的垃圾收集器开销。
# 获取对象大小
print(sys.getsizeof(True))
print(sys.getsizeof('a'))
print(sys.getsizeof('abc'))

print(sys.getsizeof('我'))
# 2
print(sys.getsizeof('我们啊'))

s = '我们啊a, #'
print(len(s))
print(sys.getsizeof(s))


