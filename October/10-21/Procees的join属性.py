# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/21 11:19

import os
import time
import random
from multiprocessing import Process


def task(name):
    print("%s %s is piaoing" % (name, os.getpid()))
    time.sleep(random.randint(1, 5))
    print("%s %s is piaoend" % (name, os.getpid()))


if __name__ == '__main__':
    li = []
    for i in range(4):
        li.append(Process(target=task, args=(i,)))

    for j in li:
        j.start()

    for j in li:
        j.join()

    print("这是主进程")



# import os
# import time
# import random
# from multiprocessing import Process
#
#
# def task(name):
#     print("%s %s is piaoing" % (name, os.getpid()))
#     time.sleep(random.randint(1, 5))
#     print("%s %s is piaoend" % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=("liusir",))
#     p2 = Process(target=task, args=("小白",))
#     p3 = Process(target=task, args=("black_boy",))
#     p4 = Process(target=task, args=("小蔡",))
#
#     p1.start()
#     p1.join()
#
#     p2.start()
#     p2.join()
#
#     p3.start()
#     p3.join()
#
#     p4.start()
#     p4.join()
#
#     print("这是主进程")



import os
import time
import random
from multiprocessing import Process


def task(name):
    print("%s %s is piaoing" % (name, os.getpid()))
    time.sleep(random.randint(1, 5))
    P = Process()

    print("%s %s is piaoend" % (name, os.getpid()))


if __name__ == '__main__':
    p1 = Process(target=task, args=("liusir",))
    p1.start()

    print(p1.is_alive())
