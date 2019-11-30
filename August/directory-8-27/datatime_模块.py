# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/27 13:57

import datetime
import time

# print(time.strptime("2019-08-27 13:58:40.258622".rsplit(".", 1)[0], "%Y-%m-%d %X"))

# ####################################################################
# res = datetime.date(year=2019, month=8, day=27)
# print(res.year)
# print(res.month)
# print(res.day)
# print(type(res))  # <class 'datetime.date'>

# ####################################################################
# res = datetime.time(**{"hour": 13, "minute": 58, "second": 40})
# print(res.hour)
# print(res.minute)
# print(res.second)
# print(type(res))  # <class 'datetime.time'>
# ####################################################################
# print(datetime.datetime)  # <class 'datetime.datetime'>

# ho = datetime.datetime.hour
# ####################################################################

# print(datetime.timedelta())


# d = datetime.datetime.now()
# print("原来的", d.today())
# print(d.timestamp())
# print(d.today())
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.timetuple())
# ####################################################################

# res = d.replace(year=2999, month=11, day=30)  # 返回一个新的时间对象

# print(res.today())  # 2999-11-30 14:32:37.730159     # 2019-08-27 14:33:19.666558

# print(datetime.date(2999, 11, 30))

# ####################################################################
# print(datetime.timedelta(2017, 10, 5, 12, 53, 35, 276589).days)
# print(datetime.timedelta(2017, 10, 5, 12, 53, 35, 276589).max)
# print(datetime.timedelta(2017, 10, 5, 12, 53, 35, 276589).min)
# ####################################################################

# print(datetime.datetime(2017, 10, 5, 12, 53, 35, 276589))

# ####################################################################

# datetime.datetime.now() + datetime.timedelta(4)  # 当前时间 +4天
# print(datetime.datetime.now() - datetime.timedelta(hours=4)) # 当前时间+4小时

# ####################################################################

# print(datetime.datetime.now() + datetime.timedelta(days=2, hours=8))

# 2019-08-29 22:35:02


# print(time.time())
# #
# # print(datetime.datetime.now().timestamp())

# #####################################时间的转换###############################
# res = datetime.datetime.now()
#
# print(res)
# ret = res.timestamp()  # 转换成时间戳
# print(ret)
# print(datetime.date.fromtimestamp(1566888190.790368))

# "2019-08-27 14:43:14.714593"

# #####################################时间的转换###############################

# print(datetime.datetime.now() + datetime.timedelta(4))  # 当前时间 +4天

"asbbcdvcsa"
# 给定一个字符串  返回这个字符串中， 不重复字符的 第一个的索引











