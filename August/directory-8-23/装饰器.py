# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/23 14:05

#########################################################################

# def home():
#     print("---首页----")
#
# def america():
#     print("----欧美专区----")
#
# def japan():
#     print("----日韩专区----")
#
# def henan():
#     print("----河南专区----")


# america()

#########################################################################

# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }

# def login():
#     if not account["is_authenticated"]:
#         username = input("请输入用户名:")
#         pwd = input("请输入密码:")
#         if account["username"] == username and account["password"] == pwd:
#             account["is_authenticated"] = True
#             print("欢迎光临")
#         else:
#             print("用户名或者密码错误")
#     else:
#         print("用户已经通过验证......")
#
# def home():
#     print("---首页----")
#
# def america():
#     print("----欧美专区----")
#
# def japan():
#     login()  # 执行前加上验证
#     print("----日韩专区----")
#
# def henan():
#     login()  # 执行前加上验证
#     print("----河南专区----")
#
#
# america()
# japan()
#
# henan()

############################################################

# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }
#
#
# def login(func):
#     if account["is_authenticated"] is False:
#         username = input("user:")
#         password = input("pasword:")
#         if username == account["username"] and password == account["password"]:
#             print("欢迎光临")
#             account["is_authenticated"] = True
#         else:
#             print("用户名或者密码错误")
#
#     if account["is_authenticated"] is True:  # 主要改了这
#         func()  # 认证成功了就执行传入进来的函数
#
# def home():
#     print("---首页----")
#
# def america():
#     print("----欧美专区----")
#
# def japan():
#     print("----日韩专区----")
#
# def henan():
#     print("----河南专区----")
#
# home()
# america = login(america)  # 需要验证就调用 login，把需要验证的功能 当做一个参数传给login
# henan = login(henan)






############################################################

# pingfang = lambda x:x**2

# def plus(n):
#     return n+1
#
#
# plus2 = lambda x:x+1
#
# print(plus(2))
# print(plus2(2))

############################################################

# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }
#
# def login(func):
#     def inner():  # 再定义一层函数
#         if account["is_authenticated"] is False:
#             username = input("user:")
#             password = input("pasword:")
#             if username == account["username"] and password == account["password"]:
#                 print("welcome login....")
#                 account["is_authenticated"] = True
#             else:
#                 print("wrong username or password!")
#         if account["is_authenticated"] is True:
#             func()
#     return inner  # 注意这里只返回inner的内存地址，不执行
#
# @login
# def america():
#     print("----欧美专区----")
# @login
# def henan():
#     print("----河南专区----")

# print(america.__name__)
# america()

# print(america)  # <function login.<locals>.inner at 0x00000000021AD950>






