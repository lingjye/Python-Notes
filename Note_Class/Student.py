#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

'''
访问限制, 类与实例属性
私有并不是真正的私有, 通过"_类名__属性名称"依然可以访问
'''

class Student(object):

	count = 0
	number = 0

	def __init__(self):
		self.name = 'Michael'
		self.count += 1
		self.__age = 18
		Student.number += 2

	def study(self):
		print('Study')

	def __study(self):
		print('Study')


print(Student.count, Student.number)
s = Student()
print(s.count, s.number)
print(Student.count, Student.number)

s.study()

# print(s.__age)
print(s._Student__age)
# s.__study()
s._Student__study()