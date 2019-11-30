# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 14:43

from gevent import monkey;monkey.patch_all()

#
# import time
#
#
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
#
# def producer():
#     '''任务2:生产数据'''
#     res = []
#     for i in range(10000000):
#         res.append(i)
#     return res
#
#
# start = time.time()
#
# # 串行执行
# res = producer()
#
# consumer(res)  # 写成 consumer(producer()) 会降低执行效率
#
# stop = time.time()
# print(stop - start)  # 1.4000067710876465


# import time
# import asyncio

# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x = yield
#         # print(x)

# def producer():
#     '''任务2:生产数据'''
#     g = consumer()
#     next(g)
#     for i in range(10000000):
#         g.send(i)
#         # print("producer")
#
#
# start = time.time()
# # 基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# # PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
# producer()
# stop = time.time()
# print(stop - start)  # 1.4100019931793213


# from greenlet import greenlet
#
#
# def eat(name):
#     print('%s eat 1' % name)
#     g2.switch('egon')
#     print('%s eat 2' % name)
#     g2.switch()
#
#
# def play(name):
#     print('%s play 1' % name)
#     g1.switch()
#     print('%s play 2' % name)
#
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
#
# g1.switch('egon')  # 可以在第一次switch时传入参数，以后都不需要


# import time
#
#
# def f1():
#     res = 1
#
#     for i in range(100000000):
#         res += i
#
#
# def f2():
#     res = 1
#
#     for i in range(100000000):
#         res *= i
#
#
# start = time.time()
#
# f1()
#
# f2()
#
# stop = time.time()
#
# print('run time is %s' % (stop - start))  # 10.985628366470337

# 切换

# from greenlet import greenlet
# import time
#
#
# def f1():
#     res = 1
#     for i in range(10000000):
#         res += i
#         g2.switch()
#
#
# def f2():
#     res = 1
#     for i in range(10000000):
#         res *= i
#         g1.switch()
#
#
# start = time.time()
#
#
# g1 = greenlet(f1)
# g2 = greenlet(f2)
#
#
# g1.switch()
#
#
# stop = time.time()
# print('run time is %s' % (stop - start))  # 52.763017892837524


import gevent
import time


def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')

g1.join()
g2.join()

# 或者gevent.joinall([g1,g2])
print('主')
