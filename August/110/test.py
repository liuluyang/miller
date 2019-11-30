# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/31 11:09

# li = [1, 2, 3]
# li2 = [4, 5, 6]
# print(li + li2)
# li.extend(li2)
# print(li)

# del li2[2]
# print(li2)

# li2.remove()


# print("%d"%-5)


# n = 5
# n+=1
# print(n)

# name = "miller"
#
# print(id(name))


# print(int("123456"))
# print(int(123.456))
# print(int("123"))


# print(bool(None))


# print(1 and 0 or 2)

# n = 1
# while True:
#     if n % 2 == 0:
#         continue
#     else:
#         print(n)
#     n += 1


# li = [1, 2, 3, 4, 6, 7, 8, 9]

# print(li[2:4])
# print(li[1::3])

# print(li[-8::2])
# print(li[::-1])

# li.reverse()
# print(li)


# name = "'mi'  '' 'er,' 'iusir'"

# print(name.split("l", maxsplit=123))


# name = "miller"

# print(name.center(50,))
#


# names = ['alex','jack','rain']

# print("\\".join(names))

# dic = {"name":"miller"}
# dic = dict([["name", "miller"],["name1", "miller"],["name2", "miller"],["name3", "miller"],["name4", "miller"],["name5", "miller"]])

# print({}.fromkeys([1, 2, 3, 4, 5, 6, 7, 8], 100))

# print(dict(zip([1, 2, 3, 4, 5, 6], ["a", "b", "c", "d", "e", "f"])))

# dic = {}
# print(dic.setdefault('olddriver',{}))

# print(dic)


# dic = {i:i*2 for i in range(1, 101)}

# dic = {
#     "miller": {"name": "miller", "age": 23, "position": "CEO", "phone": 1313838438, "salary": 2},
#     "liusir": {"name": "miller", "age": 23, "position": "CEO", "phone": 1313838438, "salary": 2},
# }

#
#
# print()
#
# choice = input(">>>")
# print(dic.get(name).get(choice))

# name = input(">>>")
# user_info = dic.get(name)
# if user_info:
#     print(user_info)
#     choice = input(">>>")
#     print(user_info.get(choice, "没有找到"))
# else:
#     print("没找到")


# A = {i for i in range(1, 11)}
# B = {i for i in range(5, 15)}
# print(A)
# print(B)


# print(A & B)
# & 交集

# print(A | B)
# | 并集

# print(A - B)
# print(B - A)
# -  差集

# print(A ^ B)
# ^ 对称差集
# "------------------------------------------------------------"
# print(A.symmetric_difference_update(B))
# print(A)

# A.intersection_update(B)
# print(A)

# A.difference_update(B)
# print(A)

# A.update(B)
# print(A)

"------------------------------------------------------------"

# C = {1, 2, 3}
# C.add([1, 2, 3, 4])
# C = frozenset(C)
# set11 = set()
# set11.add(C)
"------------------------------------------------------------"

# li = [[123], [456], [789], {"aaa":123}, 123456]
# li1 = li.copy()

# print(li)
# print(li1)
# print("------------------------------------------------------------")
# li1[1] = 55555555
# print(id(li1[1]))
# print(id(li[1]))
# print("------------------------------------------------------------")
# li1[1][0] = 55555555
# print(li1)
# print(li)

# from copy import deepcopy

# li1 = [[123], [456], [789], {"aaa": 123}, 123456]
# li2 = deepcopy(li1)

# li2[1][0] = 555555
# print(li2)
# print(li1)
# 111111

# print(1*2**5 + 1*2**4 +1*2**3 + 1*2**2 + 1*2**1 + 1*2**0)
# print(50)
# print(5*8**1 + 0*8**0)
# print(5*16**1 + 0*16**0)

# print(int("111111", 2))
# print(1*2**5 + 1*2**4 + 1*2**3 + 1*2**2 + 1*2**1 + 1*2**0)
# 50     50
# 50     40
# 50     80
# 5A
# print(5*16**1 + 10 * 16 ** 0)


# with open("./test", "r+") as f:
#     f.seek(10)
#     f.truncate()
#     # f.write()
#     # f.flush()


# def func(x, y, z=10):
# print(x, y, z)

# func(10, 5)
# func(10,20, z=20,)


# def func(*args, **kwargs):
#     print(*args, kwargs.items())


# func(1, 2, 3, 4, 6, x=10, y=20, z=30)
# func(1, 2, 3, 4, 6, **{"x":10})

# def func1():
#     return {"x":10}

# func(*[1, 2, 3, 4, 6], **{"x":10})


# func(*[1, 2, 3, 4, 6], **func1())
#
# func(1, 2, 3, 4, 6, x=10)

#
# def func(x, y, z=10, *args, **kwargs):
#     print(x, y, z)
#     print(args, kwargs)


# li = [1, 2, 3, 4, 6]
# dic = {"x": 5, "y": 10, "xxxxx": 15}

# func(*li, dic)  # x=5,y=10,z=15


# def show_info(*args, **kwargs):
#     '''只需要一个用户名'''
#     print("show_info", args, kwargs)

# def transaction(*args, **kwargs):
#     user_name = args[0]
#     other_user_name = input(">>>")
#     print(user_name, other_user_name)

#
# controller = {
#     "1":show_info,
#     "2":transaction
# }
# msg = '''
#     1:展示用户信息
#     2:交易
# '''
#
# print(msg)
#
# option = input(">>>")
#
# user_name = "miller"
#
# user_name, other_user_name = "miller", "liusir"
#
# controller[option](user_name, other_user_name)

# name = "miller"
# def func():
#     global name
#     name = "liusir"
#     print("局部的",name)
# func()
# print("全局的",name)


# name = ["miller"]


# def func():
#     name[0] = {"liusir"}
#     print("局部的",name, id(name))


# func()
# print("全局的",name, id(name))


# name = "miller"
# def wapper():
#     name = "liusir"
#     def inner():
#         name = "alex"
#     print(locals())
# wapper()


"""0,1,1,2,3,5,8,13,21"""

# def fib(num):
#     a, b = 0, 1
#     while a < num:
#         print(a, end="  ")
#         a, b = b, a+b


# def fib(num, a=0, b=1):
#     if a < num:
#         print(a, end="  ")
#         a, b = b, a + b
#         fib(num, a, b)


# fib(100000000000000)


# level = 'L0'
# n = 22

# def func():
#     level = 'L1'
#     print("func:", locals(), )
#     print(int(str(globals()["func"]).split("0x")[-1].replace(">", ""), 16))
#
#     def outer():
#         level = 'L2'
#         print("outer:", locals(), n)
#         def inner():
#             level = 'L3'
#             print("inner:", locals(),n)  # 此外打印的n是多少？
#         inner()
#     outer()
# func()


# print()
# print(id(func))

# ########################## 装饰器有参数 被装饰的函数没有参数 #####################
all_method = {}


def wapper1(num):
    def inner(func):
        if isinstance(num, str):
            all_method[num] = func
        else:
            raise TypeError("你他妈输错了")
        return func

    return inner


@wapper1("1")
def show_goods_info():
    print("from show_goods_info")


show_goods_info.text = "展示用户信息"

# @wapper1("2")
# def pay():
#     print("from pay")
# pay.text = "付款"


# n = wapper1("1")
# pay = n(pay)


# ########################## 装饰器 和 被装饰的函数都没有参数 #####################
# import time
#
# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         print(time.time() - start_time)
#     return inner
#
# @timer
# def today_sleep():
#     time.sleep(1)


# today_sleep = timer(today_sleep)

# today_sleep()

# ########################## 装饰器 和 被装饰的函数都有参数 #####################
# username = "miller"
# pwd = "123"

# from typing import Iterable
# print(isinstance([1, 2, 3, 4, 5], Iterable))


# def login(user, passwrd):
#     def outer(func):
#         @functools.wraps(func)  # 只起到 返回原函数对象的作用
#         def inner(*args, **kwargs):
#             func(*args, **kwargs)
#         return inner
#     return outer


# @login("miller", 123)
# def pay(method):
#     if method == "huabei":
#         print("调用花呗接口")
#     elif method == "zhifubao":
#         print("调用余额宝接口")
#
# print(pay)
# pay.text = "支付方式"


# login 装饰器, 支持多种方式登录  QQ  wechat

account = {"QQ": {"user": "miller", "pwd": "123"}, "wechat": {"user": "alex", "pwd": "456"}}
steel_safe = "123456"


def login(method):
    def outer(func):
        flag = False
        user_obj = account.get(method)
        if user_obj:
            user = input("请输入账号:").strip()
            pwd = input("请输入密码:").strip()
            if user == user_obj["user"] and pwd == user_obj["pwd"]:
                flag = True
            else:
                exit("第三方登录失败")
        else:
            exit("没这个登录方式")
        def inner(*args, **kwargs):
            if flag:
                func(*args, **kwargs)
        return inner
    return outer


@login(input("请选择登录方式:"))
def spinach(safe_pwd):
    if safe_pwd == steel_safe:
        print("welcome to spinach network station")
    else:
        print("密码错误")


spinach(input("请输入保险箱密码:"))
















