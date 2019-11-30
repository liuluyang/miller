# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 16:59


from multiprocessing import Process
from threading import Thread
import time
import os


# def work():
#     res = 0
#     for i in range(100000000):
#         res *= i
#
#
# if __name__ == '__main__':
#
#     li = []
#     start = time.time()
#     for i in range(4):
#         # p = Process(target=work)  # 15.501886367797852
#         # li.append(p)
#         # p.start()
#
#         t = Thread(target=work)  # 28.73664379119873
#         li.append(t)
#         t.start()
#
#     for j in li:
#         j.join()
#     stop = time.time()
#
#     print('run time is %s' % (stop - start))


def work():
    time.sleep(2)
    print("======>>")


if __name__ == '__main__':

    l = []
    start = time.time()

    for i in range(400):
        # p = Process(target=work)  # 耗时19s多,大部分时间耗费在创建进程上
        p = Thread(target=work)  # 耗时2s多
        l.append(p)
        p.start()

    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))
