# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/22 8:34


# n = 10
#
#
# def test.py():
#     print(n)
#     n = 20
#


# test.py()


# n = "全局的"
# def test1():
#     # nonlocal n  # 嵌套才有用
#     n = "test1的局部作用域"
#     def test2():
#         n = "test2 的局部作用域"
#         def test3():
#             global n
#             print(n)
#         test3()
#     test2()
# test1()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# def test1():
#     print("from test1")
#
#
# def test2(func):
#     func()

# test2(test1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# def test1(func):
#     def test2():
#         print("from test2")
#     return func
#
# res = test1()
# res()

# def n(nx):
#     print(nx)
#     n(nx)
#
# n(2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# li = list(range(1, 100))
# m = 20

# def binary_search(li, m):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if li[mid] == m:
#             return mid
#         elif li[mid] > m:
#             right = mid-1
#         elif li[mid] < m:
#             left = mid + 1
#     else:
#         return -1

# left = 0
# right = len(li) - 1


# def recursion_binary_search(left, right, m):
#     if left <= right:
#         mid = (left + right) // 2
#         if li[mid] == m:
#             return mid
#         elif li[mid] > m:
#             print("li[mid] > m", mid)
#             return recursion_binary_search(left, mid - 1, m)
#         elif li[mid] < m:
#             print("li[mid] < m", mid)
#             return recursion_binary_search(mid + 1, right, m)
#     else:
#         return -1
#
#
# print(recursion_binary_search(left, right, 23))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# print(chr(56))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name = "miller"
#
# print(dir(name))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# print(divmod(1000, 30))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import random
# li = list(range(20, 40))
# random.shuffle(li)
# print(li)
# for index, val in enumerate(li, ):
#     if val % 2 ==0:
#         print(index)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# n = '''
# def xxx():
#     print(123456)
# xxx()
# '''
#
# exec(n)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# li = [0, 1, 23, 3, 4, 4, 5, 6, 67, 7]
#
# for i in filter(lambda x:x>10, li):
#     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# map(lambda x: x ** 2, [1, 2, 3, 43, 45, 5, 6, ])  # 输出 [1, 4, 9, 1849, 2025, 25, 36]
#
# for i in map(lambda x: x ** 2, [1, 2, 3, 43, 45, 5, 6]):
#     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# from functools import reduce

# print(reduce(lambda x, y: x+y, list(range(1, 101))))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name = 123

# print(isinstance(name, str))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name = "miller"
# n = memoryview(bytes(name, encoding="utf-8"))
# print(n)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# li = [0, 1, 23, 3, 4, 4, 5, 6, 67, 7]
# li.reverse()
# li1 = reversed(li)

# print(li)
# for i in reversed(li):
#     print(i)
#
# print(li)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# print(round(10.1566, 2))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# li = [1, 2, 3, 4]
# li1 = ["a", "b", "c", "d", "e", "f"]
#
# for i in dict(zip(li, li1)).items():
#     print(i)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# fp = open("recuresion.py", "r")
# # print(fp.read())
# data = compile(fp.read(), '', 'exec')

# exec(data)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# msg = "又回到最初的起点"
# f = open("tofile", "a")

# print(msg, "记忆中你青涩的脸\n", sep="||||||", end="", file=f)
#
# f.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # #slice
# a = list(range(20))
# print(a)
# pattern = slice(3, 8, 2)

# for i in a[pattern]:
#     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
