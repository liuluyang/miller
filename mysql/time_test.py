# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/25 14:42

'''
操作流程
1. 创建connection
2. 获取cursor
3。 执行增删改查操作
4. 处理数据
5. 关闭 cursor
6. 关闭connetion

'''
import datetime
import time
import pymysql

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123", database="db1", charset="utf8")

# 获取course
cursor = conn.cursor()

sql = "select * from shijian"

cursor.execute(sql)
result = cursor.fetchall()


for row in result[0]:
    if not isinstance(row, datetime.timedelta):
        time_str = datetime.datetime.strftime(row, "%Y-%m-%d %X")  # 将datatime类型的数据, 转换成字符串时间
        time_struct = time.strptime(time_str, "%Y-%m-%d %X")  # 将字符串时间转换成 时间九元组
        mk_time = time.mktime(time_struct)  # 将时间九元组转换成  时间戳
        date_time = datetime.datetime.fromtimestamp(mk_time)  # 将时间戳 转换成datetime时间
        print(row, type(date_time), date_time, mk_time)
    else:
        print(row, type(row))
cursor.close()
conn.close()


