#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/14 11:02

# name = "这是全局变量 name"

# def change_name():
#     name = "change_namer 局部变量"
#     def inner():
#         # global name    # 如果声明了这句的话，使用的就会是最外层的 name
#         # nonlocal name
#         name = "inner 局部变量"  # 如果这里注释了打印啥？
#         print("第三层打印：", name)
#     print("第二层打印：", name)

# change_name()

#######################################################################################
# name = "这是全局变量 name"

# def change_name():
#     name = "change_namer 局部变量"
#     def inner():
#         # global name    # 如果声明了这句的话，使用的就会是最外层的 name
#         # nonlocal name
#         name = "inner 局部变量"  # 如果这里注释了打印啥？
#         print("第三层打印：", name)
#     inner()
#     print("第二层打印：", name)
#
# change_name()

# 第三层打印： inner 局部变量
# 第二层打印： change_namer 局部变量


#######################################################################################

# name = "这是全局变量 name"
#
# def change_name():
#     name = "change_name 局部变量"
#     def inner():
#         # global name
#         # nonlocal name
#         name = 123
#         print("第三层打印：", name)
#     inner()
#     print("第二层打印：", name)
#
# change_name()


# #################################  匿名函数 #####################################################
# def calc(x, y):
#     return x ** y
# print(calc(2, 2))


# 上面的代码换成 下面这样。
# calc = lambda x, y: x**y
# # print(calc(2, 2))
# calc = lambda x, y: x**y

# res = map(lambda x: x ** 2, [1, 2, 3, 4, 5])

# for i in res:
#     print(i)

# def my_map(callable, iterable):
#     li = []
#     for i in iterable:
#         res = callable(i)
#         li.append(res)
#     return li


# res = my_map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(res)

# ######################################################################################

# def get_abs(n):
#     if n < 0:
#         n = int(str(n).strip("-"))
#     return n
#
#
# #  以一个函数作为输入的  高阶函数
# def add(x, y, func):
#     return func(x) + func(y)
#
#
# print(add(-6, -6, get_abs))


# def my_len():
#     return len

# res = my_len()

# print(res([1,2,3]))


# def calc(n):
#     print(n)
#     res = int(n) // 2
#     if res == -1:
#         return
#     else:
#         calc(res)
#         print(n)
# calc(10)

#################################################################

# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, "-->", c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, "-->", c)
#         hanoi(n - 1, b, a, c)


# hanoi(4, "A", "B", "C")   # 第一层
#           a     b    c

#################
# hanoi(3, "A", "C", "B",)  #
#            a    b   c

# #####################
# hanoi(2, "A", "B", "C")
#           a    b    c

# #####################
# hanoi(1, "A", "C", "B")
#            a    b   c

# A --> B


# ####################################################################

# def calc(n):                      # 10
#     res = int(n) // 2
#     if res == 0:
#         return
#     else:
#         def calc(res):              # 5
#             res = int(n) // 2
#             if res == 0:
#                 return
#             else:
#                 def calc(res):      # 2
#                     res = int(n) // 2
#                     if res == 0:
#                         return
#                     else:
#                         def calc(res): ##### 1
#                             res = int(n) // 2
#                             if res == 0:
#                                 return
#                             else:
#                                 def calc(res):  #    0
#                                     res = int(n) // 2
#                                     if res == 0:
#                                         return
#                                     else:
#                                         calc(res)








