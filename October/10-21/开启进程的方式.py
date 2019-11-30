# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/21 11:06

import time
import random
from multiprocessing import Process,current_process


def piao(name):
    print(" %s piaoing" % name, current_process().name)
    time.sleep(random.randint(1,5))
    print(" %s piaoend" % name)


if __name__ == '__main__':
    p1 = Process(target=piao, args=("小白",), name="111111")
    p2 = Process(target=piao, args=("liusir",), name="222222")
    p3 = Process(target=piao, args=("陈亚奇",), name="333333")

    p1.start()
    p2.start()
    p3.start()


# import time
# import random
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def piao(self, name):
#         print(" %s piaoing" % name)
#         time.sleep(random.randint(1,5))
#         print(" %s piaoend" % name)
#
#     def run(self):
#         self.piao(self.name)
#
#
# if __name__ == '__main__':
#     p1 = MyProcess("小白")
#     p2 = MyProcess("liusir")
#     p3 = MyProcess("陈亚奇")

    # p1.start()
    # p2.start()
    # p3.start()




