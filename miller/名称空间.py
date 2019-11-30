# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/24 16:53

# x = 30
# def func1():
#     x = 10
#     def func2():
#         x = 20
#
#     print(locals())
#
#
# # print(dir(globals()["__builtins__"]))
#
# func1()
# print(globals())



# level = 'L0'
# n = 22
# def func():
#     level = 'L1'
#     # n = 33
#     print("func:", locals())
#     def outer():
#         # n = 44
#         level = 'L2'
#         print("outer:",locals(),n)
#         def inner():
#             level = 'L3'
#             print("inner:",locals(), n) #此外打印的n是多少？
#         inner()
#     outer()
# func()

# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }
#
#
# def login():
#     if account["is_authenticated"] is False:
#         username = input("user:")
#         password = input("password:")
#         if username == account["username"] and password == account["password"]:
#             print("welcome login....")
#             account["is_authenticated"] = True
#         else:
#             print("wrong username or password!")
#     else:
#         print("用户已登录，验证通过...")
#
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
#     login()
#     print("----河南专区----")
#
#
# home()
# henan()



account = {
    "is_authenticated":False,# 用户登录了就把这个改成True
    "username":"miller", # 假装这是DB里存的用户信息
    "password":"123" # 假装这是DB里存的用户信息
}


def login(func):
    def inner():
        if account["is_authenticated"] is False:
            username = input("user:")
            password = input("pasword:")
            if username == account["username"] and password == account["password"]:
                print("welcome login....")
                account["is_authenticated"] = True
            else:
                print("wrong username or password!")
        if account["is_authenticated"] is True:  # 主要改了这
            func()  # 认证成功了就执行传入进来的函数
    return inner

def home():
    print("---首页----")
def america():
    print("----欧美专区----")
def japan():
    print("----日韩专区----")

@login
def henan():
    print("----河南专区----")


henan = login(henan())

