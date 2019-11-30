# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/22 14:40

import time
import random
from multiprocessing import Process, JoinableQueue


def producer(q, name, food):
    for i in range(5):
        time.sleep(1)
        res = "%s %s" % (food, i)
        q.put(res)
        print('\033[45m %s 生产了 %s\033[0m' % (name, res))
    q.join()


def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue(5)
    p1 = Process(target=producer, args=(q, "liusir", "包子"))  # 生产者
    p2 = Process(target=producer, args=(q, "miller", "蛋糕"))  # 生产者
    p3 = Process(target=producer, args=(q, "yaqi", "泔水"))  # 生产者

    c1 = Process(target=consumer, args=(q, "小白"))  # 消费者
    c2 = Process(target=consumer, args=(q, "建波1号"))  # 消费者
    c3 = Process(target=consumer, args=(q, "建波2号"))  # 消费者
    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    c1.start()
    c2.start()
    c3.start()

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("主")