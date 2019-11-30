# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/25 16:41

# import datetime
# import time

# time_str = datetime.datetime.fromtimestamp(time.time())

# datetime.datetime
# datetime.date
# datetime.timedelta


import pymysql

conn = pymysql.Connection(host="localhost", port=3306, user="root", password="123", db="db1")
cursor = conn.cursor()

data = {"name": "miller11 or 1=1", "age": 20}
# data = {"name": "'miller11' or '1=1'", "age": 20}
# data = {"name": "miller'/*", "age": 20}

query_str = " and ".join(["{}={!r}".format(k, v) for k, v in data.items()])
print(query_str)
cursor.execute("select * from t1 where %s" % query_str)
res = cursor.fetchall()
print(res)

cursor.close()
conn.close()

