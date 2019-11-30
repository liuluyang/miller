# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 10:57


import time
from multiprocessing import Process, current_process
from threading import Thread
import os


# 1. 谁的开销大

# def work():
#     print("runing")
#     time.sleep(2)
#     print("end")
#
#
# if __name__ == '__main__':
#     # p1 = Process(target=work)
#     # p1.start()
#
#     t1 = Thread(target=work)
#     t1.start()
#
#     print("主")

# 2. 共享空间

# n = 100

# def change():
#     global n
#     time.sleep(1)
#     n = 0

# if __name__ == '__main__':
    # p1 = Process(target=change)
    # p1.start()
    # t1 = Thread(target=change)
    # t1.start()
    # t1.join()
    #
    # print("主:", n)


# 3. pid

# def get_ident():
#     # print("子线程的PID号: %d" % os.getpid())
#     print("子进程的PID号: %d" % os.getpid())
#     print("子进程的父进程的PID号: %d" % os.getppid())
#
#
# if __name__ == '__main__':
#     p1 = Process(target=get_ident)
#
#     p1.start()
#
#     # t1 = Thread(target=get_ident)
#     # t1.start()
#
#     print("主线程的PID:", os.getpid())



