#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

import re

test_date = '他的生日是2016-1-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.2016/12/25, .11:39, 12:39:59.223'

test_datetime = '他的生日是2016-12-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.11:34'

# date
mat = re.findall(r"\d{4}[./-]\d{1,2}[./-]\d{1,2}|\d{2}:\d{2}:\d{2}|\d{2}:\d{2}", test_date)
print(mat)
