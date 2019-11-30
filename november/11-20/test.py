# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/20 9:09


import pymysql

conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="123", db="db10", autocommit=False)

cursor = conn.cursor()
cursor.executemany("insert into actor(name) values (%s)", args=("miller2", "miller3","miller4","miller5","miller6"))

cursor.close()
conn.close()







