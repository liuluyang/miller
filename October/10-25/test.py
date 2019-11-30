# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 8:57


from multiprocessing import Pipe, Process


def work_par(write):
    write.send("我是你爸爸！")


def work_sub(read):
    print("from work_par: ", read.recv())


if __name__ == '__main__':
    read, write = Pipe()
    p1 = Process(target=work_par, args=(write,))
    p2 = Process(target=work_sub, args=(read,))

    p1.start()
    p1.join()

    p2.start()

    print("主")
