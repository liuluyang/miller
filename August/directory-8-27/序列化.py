# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/27 15:24

# py2 里面的字符串 unicode 类型   ==> 字符串
# py2 里面的字节  是 str


# py3 里面 字符串  就是unicode 编码格式的字符  str
# py3 里面的字节  就是    bytes

# ################################pickle ##################################
# import pickle

# data = {'k1': 123, 'k2': 'Hello'}

# res = pickle.dumps(data)
#
# with open("./pickle", "wb") as fp:
#     fp.write(res)
#
# with open("./pickle", "rb") as fp:
#     data_bytes = fp.read()
#     pickle.loads(data_bytes)
#     print(type(pickle.loads(data_bytes)))  # <class 'dict'>


# with open("./pickle.new", "wb") as fp:
#     pickle.dump(data, file=fp)
#
# with open("./pickle.new", "rb") as fp:
#     ret = pickle.load(file=fp)
#     print(ret)
#     print(type(ret))  # <class 'dict'>

# ################################json ##################################

import json

# data = {'k1': 123, 'k2': 'Hello'}
# res = json.dumps(data)
# print(res)
# print(type(res))  # <class 'str'>
#
# ret = json.loads(res)
# print(ret)
# print(type(ret))  # <class 'dict'>


# with open("./json.txt", "w", encoding="utf-8") as fp:
#     json.dump(data, fp=fp)


# with open("./json.txt", "r", encoding="utf-8") as fp:
#     result = json.load(fp=fp)
#     print(result)
#     print(type(result))  # <class 'dict'>


# ste1 = [1, 2, 3, 4, 5, 6, 7]
#
# print(json.dumps(ste1))

# ################### 存储中文时 ##########################
# data = {'k1': "中国", 'k2': "老牛逼了"}

# print(json.dumps(data, ensure_ascii=False))


# ################################ shelve ##################################

import shelve

# ################################ 序列化 ##################################
# f = shelve.open('shelve_test')  # 打开一个文件
#
# names = ["alex", "rain", "test.py"]
# info = {'name': 'alex', 'age': 22}
#
# f["names"] = names
# f["info"] = info
#
# f.close()

# ################################ 反序列化 ##################################
# d = shelve.open('shelve_test')  # 打开一个文件

# print(d["names"], type(d["names"]))  # ['alex', 'rain', 'test.py'] <class 'list'>
# # print(d["info"], type(d["info"]))  # {'name': 'alex', 'age': 22} <class 'dict'>
# # del d["names"]  # 删除操作

# d.close()

# ################ 修改 #######

# w = shelve.open('shelve_test')  # 打开一个文件
#
# dic = w["info"]  # 先拿到数据
# print(dic)
# dic["name"] = "liusir"  # 修改数据
#
# w["info"] = dic  # 写入文件
#
# w.close()






