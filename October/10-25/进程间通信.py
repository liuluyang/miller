# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/25 9:27


from multiprocessing import Process, Manager, Value, Queue


def change1(dic, x, y):
    print(id(dic), "11111111111")
    dic["first"] = [1, 2, 3, 4]
    dic["second"][1] = x
    dic[y] = "third"


def change2(dic):
    print(id(dic))
    dic["first"][2] = "aaaa"


if __name__ == '__main__':
    Dict = Manager().dict()
    Dict["second"] = [1, 2.3]

    p1 = Process(target=change1, args=(Dict, "xxxx", "yyyy"))
    p1.start()
    p1.join()

    p2 = Process(target=change2, args=(Dict,))
    p2.start()


