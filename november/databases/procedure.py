# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/31 16:46


import time
import pymysql
import datetime

# autocommit=True 在链接数据库的时候, 可以设置上这个参数, 否则在执行插入等命令的时候，需要显示的执行 conn.commit()
# 这个命令就是用来, 控制执行的命令  是否要提交到真实的数据库中。
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123")

cursor = conn.cursor()
# cursor.execute("show databases")
conn.select_db("db2")  # 切换数据库

# cursor.execute("select * from blog")  #
#
# cursor.callproc("p2", ("alex",))
#
# cursor.execute("select * from blog")
# print(cursor.fetchall())


'''程序中调用过程时, 所需的参数, 会自动的进行创建, 按照顺序 @_过程名_所需要参数的索引(从0开始)'''
# cursor.callproc("p3", (1, 3, 0))  # @_p3_0  @_p3_1  @_p3_2
# result = cursor.fetchall()
#
# tu = result[0][2].timetuple()  # 转换为时间9元组
# print(time.mktime(tu))
#
# cursor.execute("select @_p3_0,@_p3_1,@_p3_2")


'''execute 中 args 的使用. 这种方式只能够插入 一条数据'''
# data = (3, "miller3", datetime.datetime.now())
# cursor.execute("insert into blog values(%s, %s, %s)", args=data)
#
# cursor.execute("select * from blog")
# conn.commit()  # execute 只是执行而已, 要将数据提交之后, 才能真正的保存到数据库
# print(cursor.fetchall())


# '''executemany 插入多条数据'''
data = (
    (4, "miller4", datetime.datetime.now()),
    (5, "miller5", datetime.datetime.now()),
    (6, "miller6", datetime.datetime.now()),
)

cursor.executemany("insert into blog values (%s, %s, %s)", args=data)

cursor.execute("select * from blog")
conn.commit()  # 一定要提交
print(cursor.fetchall())

