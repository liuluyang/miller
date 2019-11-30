# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/31 21:21

import time


# print(date)
nine_time = time.gmtime(1573091159)  # 将时间戳传换成 时间九元组

res = time.strftime("%Y-%m-%d %X", nine_time)  # 将时间九元组  转换成, 字符串时间
print(res)

# res = time.strptime(res, "%Y-%m-%d %X")  # 将字符串时间,按照给定的格式,抓换成 时间九元组
# print(res)

# desc = time.mktime(res)  # 将时间九元组 转换成, 时间戳
# print(desc)












