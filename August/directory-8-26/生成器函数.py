# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/26 9:38


# def fib(max):
#     a, b = 0, 1
#     n = 0
#     while True:
#         n = a + b
#         a = b
#         b = n
#         yield n


# print(fib)  # <function fib at 0x00000000004CC1E0>
# print(fib(100))  # <generator object fib at 0x00000000020A2C00>


# gen = fib(10)

# ####################生产者  消费者模型 ################################
# import asyncio
# import time
# import random

# def consumer(name):
#     print("%s 准备吃包子啦!" % name)
#     while True:
#         baozi = yield name  # yield可以接收到外部send传过来的数据并赋值给baozi
#         print("包子[%s]来了,被[%s]吃了!" % (baozi, name))
#         time.sleep(1)


# c1 = consumer("李建波")
# c2 = consumer("王昱斌")
# c3 = consumer("李贺")
# name = c1.__next__()
# c2.__next__()
# c3.__next__()

# for i in range(10):
#     res = c1.send(i)

# from typing import Iterable

# print(isinstance("abc", Iterable))
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(set(), Iterable))
# print(isinstance(tuple(), Iterable))
# print(isinstance(100, Iterable))


# from typing import Iterator  # 迭代器

# print(isinstance("abc", Iterator))   # False
# print(isinstance([], Iterator))     # False
# print(isinstance({}, Iterator))   #   False
# print(isinstance((x for x in range(10)), Iterator))  # True
# print(isinstance(set(), Iterator))   # False
# print(isinstance(tuple(), Iterator))   # False
# print(isinstance(100, Iterator))   # False

# from typing import Iterator  # 迭代器

# print(isinstance(iter("abc"), Iterator))   # True
# print(isinstance(iter([]), Iterator))     # True
# print(isinstance({}, Iterator))           # False
# print(isinstance((x for x in range(10)), Iterator))  # True
# print(isinstance(set(), Iterator))     # False
# print(isinstance(tuple(), Iterator))   # False
# print(isinstance(100, Iterator))       # False








