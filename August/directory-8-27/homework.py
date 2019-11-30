# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/27 8:40

# import time
#
#
# def logger(filename, channel="file"):
#     '''
#     :param filename:  log filename
#     :param channel: 输出目的: 屏幕(terminal) 文件 (file) 屏幕+文件(both)
#     :return:
#     '''
#     import os
#     if not os.path.exists(filename):
#         return
#
#     fp = open(filename, "a", encoding="utf-8")
#     count = 0
#     while True:
#         text = yield
#         write_time = time.strftime("%Y-%m-%d %X", time.localtime())
#         text = "%s [%s] %s" % (write_time, count, text)
#         count += 1
#         if channel == "file":
#             print(text, file=fp)
#         elif channel == "terminal":
#             print(text)
#         elif channel == "both":
#             print(text, file=fp)
#             print(text)
#
#
# logge = logger(r"D:\education_project\user_info", channel="both")
# logge.__next__()
# logge.send("text0")
# logge.send("text1")


# 9._写函数，传入一个参数n，返回n的阶乘_
# 例如:cal(7)
# 计算7654321

# def cal(x):
# from functools import reduce
# li = list(range(1, x + 1))
# return reduce(lambda x, y: x * y, li)

# if x == 1:
#     return 1
# return x * cal(x-1)


# print(cal(7))

# ###########################################################################
import sys

# result = sys.argv
# print(result)
#
#
# def cal(x):
#     if x == 1:
#         return 1
#     return x * cal(x-1)
#
# print(cal(int(result[1])))

# ###########################################################################

# sys.exit("")  # 退出的

# ###########################################################################

# print(sys.version)

# ###########################################################################

# import os

# print(os.name)
#
# print(sys.maxsize)
#
# print(sys.platform)

# ###########################################################################


# sys.stdout.write("123456798")
# sys.stdout.write("\x08" * len("123456798"))
# sys.stdout.write("123456798")
# sys.stdout.write("\x08" * len("123456798"))
# sys.stdout.write("123456798")

# print("\r123456798", end="")
# print("\r123456798", end="")
# print("\r123456798", end="")
# print("\r123456798", end="")

# print(sys.stdout.write("请输入内容"))
#
# res = sys.stdin.readline()
# print(res)

# res = input()
# # print(res)

# print(sys.getdefaultencoding())

# print(sys.getfilesystemencoding())

# ###########################################################################
import time
# res = time.strptime("2017-10-3 17:54","%Y-%m-%d %H:%M")
# 输出 time.struct_time(tm_year=2017, tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54, tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=-1)
# time.strptime # 讲一个字符串时间, 通过指定的格式， 转换成 9 元组

# res = time.mktime(res)  # 1507024440.0    # 将指定的 9 元组！转换成 时间戳

# res = time.localtime(res)  # time.struct_time(tm_year=2017, tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54, tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=0)
# time.localtime  将一个时间戳，转换成 当前市区的  9 元组

# res = time.strftime("%Y-%m-%d %H:%M:%S", res)
# print(res)  # 2017-10-03 17:54:00

