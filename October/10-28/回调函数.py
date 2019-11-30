# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 9:47
import time
import random
from concurrent import futures


def laing(name):
    print("%s is laing" % name)
    num = random.randint(1, 5)
    time.sleep(num)
    return num, name


def width(res):
    result = res.result()
    print("           %s la le %s斤" % (result[1], result[0]))


executor = futures.ThreadPoolExecutor(10)

# res = executor.map(laing, ["xiaobai", "xiaocai", "alex", "egon", "kevin", "liusir"])

# for i in res:
#     width(*i)


for name in ["xiaobai", "xiaocai", "alex", "egon", "kevin", "liusir"]:
    executor.submit(laing, name).add_done_callback(width)

