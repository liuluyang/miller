# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/19 16:51

# n = 100
# while n > 0:
#     n = int(n / 2)
#     print(n)


# def calc(x):
#     if x > 0:
#         x = int(x / 2)
#         print(x)
#         calc(x)


# def calc(n):
#     n = int(n / 2)
#     print(n)
#     if n > 0:
#         calc(n)
#     print(n)
#     return None
#
#
# calc(100)

# import sys
#
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(2000))
# print(sys.getrecursionlimit())

# li = ""
#
# print(all(li))

# li = [{},[],0,""]
# print(any(li))


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for ind, val in enumerate(li, 1):
#     print(ind, val)


# print(eval("1+1"))


# print(isinstance(6541654, int))

# li = [2, 5, 6, 4, 3, 65, 7, 9, 41, 5, 6, 4, 6, 4, 5]
#
# new_li = sorted(li)
# print(li)
# print(new_li)

# msg = "又回到最初的起点"
# f = open("tofile", "w")
# print(msg, "记忆中你青涩的脸", sep="|", end="", file=f)


# import pickle
#
#
# dic = {"name":"miller", "age":26}
# diccc = {"dic":dic, "old":555555}
#
# li = [dic, diccc]
#
# with open("./staff", "wb") as f:
#     f.write(pickle.dumps(li))
#
#
# with open("./staff", "rb") as f:
#     print(pickle.loads(f.read()))


# for i in range(100, 1000):
#     a, b = divmod(i, 100)
#     c, d = divmod(b, 10)
#     if a > 5 or c > 5 or d > 5:
#         continue
#     if (a + c + d) == 5:
#         print(i)
import os

for i in range(1, 20):  # 公鸡
    for j in range(1, 33):  # 母鸡
        for n in range(1, 300):  # 小鸡
            if i * 5 + j * 3 + (1/3) * n == 100 and i+j+n == 100:
                print(i, j, n)
times = os.times()
print(times.elapsed - (times.system + times.user))




print()
