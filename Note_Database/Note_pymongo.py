#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
'''
Description

Please run cmdline :
pip install pymongo

建议使用 robo 3T 查看
'''

import pymongo

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'MyMongoDB'
MONGO_TABLE = 'MyTableName'

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]

table = db[MONGO_TABLE]

# 添加数据
# table.insert_one({'pid':1, 'name':'名称'})

# 更新数据 数据库找不到会自动添加
table.replace_one({ 'pid':1 }, {'pid':1, 'name':'名称12啊'}, True)


