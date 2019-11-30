# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/7 15:53


import pymysql

conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="123", db="db3", autocommit=True)
cursor = conn.cursor()  # 拿到游标


# def create_table(tb_name, **kwargs):
#     if tb_name and kwargs:
#         sql = "create table %s (%s)" % (tb_name,",".join(["%s %s" % item for item in kwargs.items()]))
#         print(sql)

# create_table("t6", id="int", name="varchar(10)")

sql = """insert into t6 values (5)"""
cursor.execute(sql)
# print(cursor.fetchall())


# sql = "select * from t6"
# cursor.execute(sql)

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# print(cursor.fetchall())

# print(cursor.fetchmany(-2))

cursor.close()
conn.close()



