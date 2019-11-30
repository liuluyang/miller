# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/28 11:13


# 描述符协议
# __set__   __get__  __delete__

# 覆盖描述符： 实现了 __set__ 的
# 非覆盖的： 只是实现 __get__


'''
优先级：
1. 类属性
2. 覆盖描述符
3. 实例属性
4. 非覆盖的
5. __getattr__
'''

# class Description(object):
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.types):
#             raise TypeError
#         instance.__dict__[self.name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __delete__(self, instance):
#         return instance.__dict__.pop(self.name)
#
#
# class Person(object):
#     name = Description("name", str)
#     age = Description("age", int)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Types(object):
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.types):
#             raise TypeError
#         instance.__dict__[self.name] = value
#
#     def __get__(self, instance, owner):
#         pass
#
#     def __delete__(self, instance):
#         pass
#
#
# def description(attrs):
#     def inner(cls):
#         for name, types in attrs.items():
#             setattr(cls, name, Types(name, types))
#         return cls
#     return inner
#
#
# @description({"name": str, "age": int})
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# Person("miler", "65465")


"""求 100 到 1000 之间, 各个位数相加之和等于5的数， 全部列出来"""
# for i in range(100, 1000):
#     a, b = divmod(i ,100)  # 9  99
#     c, d = divmod(b, 10)   # 9  9
#     if a > 5 or c > 5 or d > 5:
#         continue
#     if a + c + d == 5:
#         print(i)
""" A --> 1   Z-->26   随机给一个数, 求能匹配成功的数量。"""


# 109    J I
# 2 2 5   336
# B B E
# V E
# B Y


def check(s):
    s = str(s).strip()
    length = len(s)
    if length == 0:
        return 0
    li = [0 for _ in range(length+1)]
    li[0] = 1
    print(li, "首次")
    for j in range(1, length+1):
        if s[j-1] == "0":
            li[j] = 1
        else:
            li[j] = li[j-1]
        if j > 1 and (int(s[j - 2]) == 1 or int(s[j - 2]) == 2 and int(s[j-1]) <= 6):
            li[j] += li[j - 2]
        print(li)
    return li[length]


print(check(123))
