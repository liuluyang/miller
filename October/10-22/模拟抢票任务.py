# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/22 9:24


from multiprocessing import Process, Lock
import time
import json


def search_ticket(name):
    time.sleep(1)
    data = json.load(open("./ticket", "r", encoding="utf-8"))
    print("进程%d  查询到了还剩 %d 张票" % (name, data["count"]))


def get_ticket(name):
    data = json.load(open("./ticket", "r", encoding="utf-8"))
    if data["count"] >= 1:
        time.sleep(3)
        data["count"] -= 1
        json.dump(data, open("./ticket", "w", encoding="utf-8"))
        print("   进程%s 购买了一张票" % name)


def task(name, mutex):
    search_ticket(name)

    # mutex.acquire()
    get_ticket(name)
    # mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(20):
        p = Process(target=task, args=(i, mutex))
        p.start()




