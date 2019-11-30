# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 18:55


import time


# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         print(time.time() - start_time)
#     return inner
#
#
# @timer
# def test():
#     time.sleep(1)
# test()

# #####################################################################


# def timer(func):
#     def inner(name):
#         print("from inner",name)
#         start_time = time.time()
#         func(name)
#         print(time.time() - start_time)
#     return inner
#
# @timer
# def test(name):
#     time.sleep(1)
#     print("test 打印的名字是: %s" % name)
#
#
# test("miller")

# #####################################################################

def timer(age):
    def outer(func):
        def inner(name):
            print("%s 的 年龄是 %d" % (name, age))
            func(name)

        return inner

    return outer


@timer(23)
def test(name):
    print("test 打印的名字是: %s" % name)


# outer = timer(23)
# test = outer(test)

# test("miller")


# import sys
# import test
#
# for i in sys.modules.items():
#     print( i)

# n = getattr(sys.modules["test"], "write_user_info", None)


# print(n)

# import time
# n = 1
# while n < 100000000:
#     time.sleep(0.5)
#     n = n + n * 2
#     print(n)


# from functools import partial
#
# int2 = partial(int, base=2)
#
# print(int2("11111111"))










