# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/24 9:08


from threading import Thread, Semaphore, currentThread
import time


def work():
    sm.acquire()
    print("%s get sm" % currentThread().getName())
    time.sleep(3)
    sm.release()


if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(23):
        t = Thread(target=work)
        t.start()
