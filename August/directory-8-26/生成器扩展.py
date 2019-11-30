# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/26 10:39


# import itertools
#
#
# def test.py(it):
#     res = yield from it
#
#
# li = list(range(1, 21))
#
# gen = test.py(li)
#
# for i in gen:
#     print(i)


def my_http_code():
    # yield "<div>"
    # info = yield ""
    # yield "my name is miller"
    yield 123
    try:
        print(123654987613)
    except:
        print("error")


n = my_http_code()
print(next(n))

try:
    next(n)
except StopIteration:
    pass





http_code = ""
# for i in my_http_code():
#     http_code+=i

print(http_code)





