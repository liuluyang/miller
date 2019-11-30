# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/2 15:27


import pymysql

conn = pymysql.Connection(host="127.0.0.1", port=3306, user="root", password="123", db="db1")

cursor = conn.cursor()
# conn.select_db("db1")

cursor.execute("select * from sys_t")

# print(cursor.fetchone())
# print(cursor.fetchmany(2))
# print(cursor.fetchall())

print(cursor.fetchall())

cursor.close()
conn.close()

