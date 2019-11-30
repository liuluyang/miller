# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/24 9:14


# from threading import Event
#
#
# ev = Event()
#
# print(ev.isSet())
#
# ev.wait(1)
#
# ev.set()
# print(ev.isSet())
#
# ev.clear()
# print(ev.isSet())


from threading import Thread, Event, currentThread
import time
import random


def conn_mysql():
    count = 1
    while not event.isSet():
        if count > 3:
            raise TimeoutError("连接超时")
        print("<%s> 尝试 %s 连接" % (currentThread().getName(), count))
        event.wait(0.7)
        count += 1

    print('<%s>链接成功' % currentThread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % currentThread().getName())
    time.sleep(random.randint(2, 4))
    event.set()


if __name__ == '__main__':
    event = Event()
    t1 = Thread(target=conn_mysql)
    t2 = Thread(target=conn_mysql)

    c1 = Thread(target=check_mysql)

    t1.start()
    t2.start()

    c1.start()

