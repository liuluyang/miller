# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 14:02


from threading import Thread
import threading
import random
import time


def work():
    time.sleep(random.randint(1, 3))
    print(threading.current_thread().getName())

    # def work1():
    #     print(threading.current_thread().getName())
    # t3 = Thread(target=work1)
    # t3.start()


if __name__ == '__main__':
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t3 = Thread(target=work)

    t1.start()
    t2.start()
    t3.start()

    # t1.is_alive()

    print(threading.current_thread())

    print(threading.enumerate())
    print(threading.active_count())








