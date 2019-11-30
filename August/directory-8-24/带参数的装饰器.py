# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/24 9:42


# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }
# def login(func):
#     def inner(*args, **kwargs):  # 再定义一层函数
#         if account["is_authenticated"] is False:
#             username = input("user:")
#             password = input("pasword:")
#             if username == account["username"] and password == account["password"]:
#                 print("welcome login....")
#                 account["is_authenticated"] = True
#             else:
#                 print("wrong username or password!")
#         if account["is_authenticated"] is True:
#             func(*args, **kwargs)
#     return inner  # 注意这里只返回inner的内存地址，不执行
#
# def america(vip_level, is_english):
#     print("----欧美专区----")
#
# def henan(vip_level):
#     if vip_level < 3:
#         print("----河南专区普通会员----")
#     else:
#         print("欢迎来到尊贵河南口音RMB玩家私密社区".center(50, "-"))
#         print("再充值500就可以获取演员微信号，幸福大门即将开启".center(50, " "))
#
# henan = login(henan)
# henan(3)


###########################################################################

# account = {
#     "is_authenticated": False,  # 用户登录了就把这个改成True
#     "username": "miller",  # 假装这是DB里存的用户信息
#     "password": "123"  # 假装这是DB里存的用户信息
# }
#
#
# def login(nation):
#     def outer(func):
#         def inner(*args, **kwargs):  # 再定义一层函数
#             print(args, kwargs)
#             if account["is_authenticated"] is False:
#                 username = input("user:")
#                 password = input("pasword:")
#                 if username == account["username"] and password == account["password"]:
#                     print("welcome login....")
#                     account["is_authenticated"] = True
#                 else:
#                     print("wrong username or password!")
#             if account["is_authenticated"] is True:
#                 func(*args, **kwargs)
#         return inner  # 注意这里只返回inner的内存地址，不执行
#     return outer


# nation = "法国"

# @login(nation)
# def america(vip_level, is_english):
#     print("----欧美专区----")


# outer = login(nation)
# america = outer(america)
# america(3, True)






