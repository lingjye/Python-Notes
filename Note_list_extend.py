#!/usr/bin/env python
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

# 添加一个数组元素
list1 = [1, 2, 3]
list2 = [2, 3]
list2.append(list1)
print(list2)

# 追加一个数组中所有元素到本数组
x = [1, 2, 3]
x.extend([4, 5])
print(x)

# 将数组转化为字符串
list1 = ["a", "b", "c"]
print("".join(list1))
# 将字符串转化为数组
str = "abc"
list1 = [x for x in str]
print(list1)
