#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

''''
Description

pip install goto-statement

借助 goto 语句的高效性, 可以轻松的跳出深层循环

但是 尽量不用, 否则可能会导致程序混乱, 无法控制

'''

from goto import with_goto

from goto import with_goto

@with_goto
def range(start, stop):
	i = start
	result = []

	label .begin
	if i == stop:
		result.append(i)
		goto .end

	result.append(i)
	i += 1
	goto .begin
	label .end
	return result

result = range(1, 2)
print(result)
