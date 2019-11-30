# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/24 9:37


from threading import Timer


def sayhi(name, a, b,c):
    print(a, b, c)
    print("hello %s " % name)


t = Timer(2, sayhi)
t.start()

