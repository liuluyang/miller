# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/30 10:07


import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings

# filename = os.path.join(settings.USER_INFO_DIR, "three_pei")

# with open(filename, "r", encoding="GBK") as f:
#     print(f.read())


import tools

def fib(n):
    a, b = 0, 1
    while n > a:
        print(a, end="  ")
        a, b = b, a+b

fib(1000)



