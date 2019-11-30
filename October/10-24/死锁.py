# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/24 8:48


from threading import Thread, Lock
import time

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()
    def func1(self):
        mutexA.acquire()
        print('\033[45m%s 拿到A锁\033[0m' % self.name)
        mutexB.acquire()
        print('\033[45m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[33m%s 拿到B锁\033[0m' % self.name)
        mutexA.acquire()
        print('\033[33m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    mutexA = Lock()
    mutexB = Lock()
    for i in range(10):
        t = MyThread()
        t.start()
