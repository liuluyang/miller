# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/22 14:16


import time
import random
from multiprocessing import Process, Queue


#
# def producer():
#     gen = consumer()
#     next(gen)
#     n = 0
#     while n < 20:
#         print("生产者 生产了第 %d 包子" % n)
#         gen.send(n)
#         n += 1
#
#
# def consumer():
#     while True:
#         baozi = yield
#         print("消费者 消费了 第%d 个包子" % baozi)
#
# producer()


def producer(q, name, food):
    for i in range(5):
        time.sleep(1)
        res = "%s %s" % (food, i)
        q.put(res)
        print('\033[45m %s 生产了 %s\033[0m' % (name, res))


def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=producer, args=(q, "liusir", "包子"))  # 生产者
    p2 = Process(target=producer, args=(q, "miller", "包子"))  # 生产者
    p3 = Process(target=producer, args=(q, "yaqi", "包子"))  # 生产者

    c1 = Process(target=consumer, args=(q, "小白"))  # 消费者
    c2 = Process(target=consumer, args=(q, "建波1号"))  # 消费者
    c3 = Process(target=consumer, args=(q, "建波2号"))  # 消费者

    c1.start()
    c2.start()
    c3.start()

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    q.put(None)

    print("主")

