# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/22 15:31


def hanoi(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return
    hanoi(n - 1, a, c, b)
    print(a, "-->", c)
    hanoi(n - 1, b, a, c)


hanoi(3, "A", "B", "C")
