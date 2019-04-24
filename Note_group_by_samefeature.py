#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
a = [{'key':1, 'value':2},
	 {'key':2, 'value':3},
	 {'key':1, 'value':4},
	 {'key':4, 'value':5},
	 {'key':2, 'value':6},
	 {'key':None, 'value':7},
	 {'key': 1, 'value': 2},
	 {'key': 2, 'value': 3},
	 {'key': 1, 'value': 4},
	 {'key': 4, 'value': 5},
	 {'key': 5, 'value': 6},
	 {'key': 8, 'value': 7}
	 ]

c = list()

for item in a:
	find:bool = False
	for sub_list in c:
		sub_item = sub_list[0]
		if sub_item['key'] == item['key']:
			sub_list.append(item)
			find = True
			break
	if not find:
		sub_list_new = list()
		sub_list_new.append(item)
		c.append(sub_list_new)

print(c)


# from itertools import groupby
#
# a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
# b = set(a)
# c = list()
# for each_b in b:
# 	count = 0
# 	for each_a in a:
# 		if each_b == each_a:
# 			count += 1
# 			c.append(each_a)
# 	print(each_b, ": ", count)
# d = [list(v) for _, v in groupby(c)]
# print(c)
# print(d)
