# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 16:01


from threading import Thread, Lock
import time
import random


# count = 0

# def change():
#     global count
#     time.sleep(random.randint(1, 2))
#     count += 1

# if __name__ == '__main__':
#     li = []
#     for i in range(100):
#         t = Thread(target=change)
#         li.append(t)
#
#     for i in li:
#         i.start()
#     for i in li:
#         i.join()
#
#     print(count)


def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()


if __name__ == '__main__':
    n = 100

    lock = Lock()

    li = []
    for i in range(100):
        t = Thread(target=work)
        li.append(t)
        t.start()

    for j in li:
        j.join()

    print(n)


