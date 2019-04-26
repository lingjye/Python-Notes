#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
'''
Description

Please run cmdline :
pip install Cython
pip install pymmsql

注意连接SQL server一定别安装错了, 笔者就是使用了pymysql(一个字母的差别), 导致连接不上数据库
如果遇到import pymssql不提示, 可能需要重启PyCharm
'''

import pymssql
from pymssql import Cursor

SERVER_IP = 'server_ip'
UID = 'uid'
PWD = 'pwd'
DB_NAME = 'dbname'
# 连接数据库
db_client = pymssql.connect(host=SERVER_IP, user=UID, password=PWD, database=DB_NAME)
db_cursor: Cursor = db_client.cursor()

print(db_cursor)
def query():
	db_cursor.execute('''SELECT TOP 10 * FROM [dbo].[Page_Watch_Item]''')
	# row = db_cursor.fetchall()
	# print(row)
	for cur in db_cursor:
		print(cur)

# 执行存储过程
def excute():
	# db_cursor.callproc('SP_V1_Wawtch_ZYL_UpdateReportHashCodeItem')
	db_cursor.execute('exec SP_V1_Wawtch_ZYL_UpdateReportHashCodeItem')
	# db_cursor.execute(f"exec 存储过程名称 @参数1='xxx',@参数2='xxx',@参数3='xxx',@参数4='xxx'")
	# 注：变量前面要加 @，要是调用存储过程无需传参可忽略；
	# pymssql 2.0 以上可通过cursor.callproc方法调用存储过程cursor.callproc('存储过程', '参数元组')
	# 需使用cursor.nextset()
	# 才能得到结果集

	result = db_cursor.nextset() # 得到结果集
	print(result)

query()
excute()

'''
SQL 语句
'''
# 查询是否当天: (本周: weak, 本月: month, 当年: year) 结果是与当天的间隔
sql = 'select * from table where DateDiff(day,datetime,getdate())=0'

# 当前系统日期、时间 2019-03-25 11:37:10.530
sql = 'select getdate()'


'''
Example:

conn = pymssql.connect(server, user, password, "tempdb")
cursor = conn.cursor()
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

conn.close()

使用with语句
with pymssql.connect(server, user, password, "tempdb") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))

'''