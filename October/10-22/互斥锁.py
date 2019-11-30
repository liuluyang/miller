# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/22 9:07


# import multiprocessing as mp
# import os
# import time
#
#
# def task(name, mutex):
#     mutex.acquire()
#     print(" %s is runing" % os.getpid(), name)
#     time.sleep(1)
#     print(" %s is down" % os.getpid(), name)
#     mutex.release()
#
#
#
# if __name__ == '__main__':
#     mutex = mp.Lock()
#     for i in range(3):
#         p = mp.Process(target=task, args=(i, mutex))
#         p.start()


