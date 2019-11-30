# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/21 8:18


# n = "asd"

# def test.py():
#     print(n)
#     n = 10
#
# # test.py()
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# n = Person("miller", 23)
#
#
# from collections import namedtuple
#
# Person = namedtuple("Person", ["name", "age"])
#
# p1 = Person("miller", 26)
#
# print(vars(n))

import re
# "abc123"
# abc = A
# 123 = B
# "?! A 前面不是 B"  # 负前瞻,
# "?= A 的前面是 B"  # 前瞻不消耗字符, 用游标理解就是, 虽然已经读取字符判断过了, 但是游标还在原位置上。
# "?:"  # 为非捕获匹配


# n = "as456dasdsasd"
# res = re.search("(?![0-9]*$)(?![A-Za-z]*$)[a-zA-Z0-9]{8,16}", n)
# (?![0-9]*$)  #空之前不是纯数字, 并且到结尾的
# (?![A-Za-z]*$)  # 空之前不是纯字母, 并且到结尾的

# print(res)

