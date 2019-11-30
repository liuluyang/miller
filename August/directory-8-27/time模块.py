# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019\8\27 10:13


import time

# print(time.time())  # 当前时间 时间戳
# 1566872853.912672

# ###########################################################
# print(time.localtime())  # 当前时间 9 元组


# print(time.localtime(1566872853.912672))  # 得到时间9元组！ 默认当前

# ###########################################################

# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  # 将时间9元组 转换成 字符串

# print(time.strftime("%Y-%m-%d %X",time.localtime()))  # 将时间9元组 转换成 字符串

# ###########################################################

# print(time.strptime("2019-08-27 10:20:50", "%Y-%m-%d %X"))
# 将字符串格式的时间，按照指定的 format 转换成，9元组, (format 需要一一对应)

# ###########################################################
# (tm_year=2019, tm_mon=8, tm_mday=27, tm_hour=10, tm_min=27, tm_sec=33, tm_wday=1, tm_yday=239, tm_isdst=0)
# (tm_year=2019, tm_mon=8, tm_mday=27, tm_hour=2, tm_min=27, tm_sec=33, tm_wday=1, tm_yday=239, tm_isdst=0)

# res = time.gmtime()   # 得到时间9元组！ 默认当前
# print(res)  # 得到成 0 时区的， 9元组 struct_time

# res1 = time.localtime(1566872853.912672)
# print(res1)
# 1566872853.912672

# ###########################################################
# print(time.mktime(res1))  # 将9元组的时间，转换成 时间戳

# ###########################################################
# print("start")
# time.sleep(5)
# print("end")

# ###########################################################

# print(time.asctime(res1))  # Tue Aug 27 10:27:33 2019  # 需要时间9元组, 默认当前
# print(time.ctime(1566872853.912672))  # Tue Aug 27 10:27:33 2019  # 需要时间戳, 默认当前时间


# with open("./user_info", "r", encoding="utf-8")as f, open("./user_info.new", "w", encoding="utf-8") as fp:
#     for line in f:
#         pass
#         fp.write(line)
#
#     import os
#     os.replace("./user_info.new", "./user_info")

n = 'onlinedate','id','name'  #
nn = 'opentime','serverid','servername'









