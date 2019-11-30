# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/23 9:45

# name = "miller"
#
#
# def change_name(xx):
#     name = "liuser"
#     print(name)
#
# change_name(111)
#
# print(name)


# def func1():
#     name = "miller"
#     def func2():
#         print(name)
#

# import builtins
#
# print(dir(builtins))
# name = "miller"
# print(globals())

# level = 'L0'
# n = 22


# def func():
#     level = 'L1'
#     n = 33
#     print("func:", locals())
#     def outer():
#         n = 44
#         level = 'L2'
#         print("outer:", locals(), n)
#         def inner():
#             level = 'L3'
#             print("inner:", locals(), n,)  # 此外打印的n是多少？
#
#         inner()
#     outer()
#
#
# func()


# def outer():
#     n = 44
#     def inner():
#         level = 'L3'
#         print("inner:", locals(), n, )  # 此外打印的n是多少？
#     return inner
#
#
# outer()





