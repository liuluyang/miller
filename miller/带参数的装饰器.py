# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/25 16:57

# account = {
#     "is_authenticated":False,# 用户登录了就把这个改成True
#     "username":"miller", # 假装这是DB里存的用户信息
#     "password":"123" # 假装这是DB里存的用户信息
# }
#
#
# def login(func):
#     def inner(*args, **kwargs):
#         if account["is_authenticated"] is False:
#             username = input("user:")
#             password = input("pasword:")
#             if username == account["username"] and password == account["password"]:
#                 print("welcome login....")
#                 account["is_authenticated"] = True
#             else:
#                 print("wrong username or password!")
#         if account["is_authenticated"] is True:  # 主要改了这
#             func(*args, **kwargs)  # 认证成功了就执行传入进来的函数
#     return inner
#
# def home():
#     print("---首页----")
# def america():
#     print("----欧美专区----")
# def japan():
#     print("----日韩专区----")
#
#
# def henan(name):
#     print("---%s 观看 -河南专区----" % name)
#
#
# henan = login(henan)
#
# henan("河南鸭王")

# li = ["微信", "支付宝", "花呗"]
# for ind, val in enumerate(li, 1):
#     print(ind, val)


# def identification(ident):
#     def outer(func):
#         def inner(money):
#             func(money, ident)
#         return inner
#     return outer


# @identification(li[int(input(">>>"))-1])
# def pay(money, identily):
#     print(" %s 支付了 %.2f 元" % (identily, money))
#
#
# pay(25)








