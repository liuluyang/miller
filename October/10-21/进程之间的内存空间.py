# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/21 14:17

# import time
# from multiprocessing import Process
#
# n = 100
#
#
# def change_n():
#     global n
#     time.sleep(0.1)
#     n -= 1
#
#
# if __name__ == '__main__':
#     li = [Process(target=change_n) for i in range(100)]
#
#     for i in li:
#         i.start()
#
#     for i in li:
#         i.join()
#
#     print(n)
