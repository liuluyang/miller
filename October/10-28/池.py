# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 9:22


# from concurrent import futures


# print(list(map(lambda x:x*2, [1,2,3])))
#
# def work(name):
#     print("my name is %s " % name)
#     return "miller"

# with futures.ThreadPoolExecutor(50) as executor:
#     # future = executor.submit(work, "xiaobai")
#     # print(future.result(), 123123123123)
#     res = executor.map(work, ["xiaobai", "miller", "caitonzhi", "liusir"])

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import os


def work(name):
    time.sleep(2)
    print("my name is %s " % name, os.getpid())


if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=3)
    executor = ProcessPoolExecutor(max_workers=2)
    executor.map(work, ["xiaobai", "xiaocai", "miller", "liusir", "xiaobaicai"])
    executor.shutdown(wait=True)
    print("主线程")
