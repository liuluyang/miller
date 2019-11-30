#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/13 15:19


# def stu_register(name, age, course='PY' ,country='CN'):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#     if age <= 22:
#         return False
#     else:
#         return True
#
#
# registriation_status = stu_register("王山炮",22,course="PY全栈开发",country='JP')
#
# if registriation_status:
#     print("注册成功")
# else:
#     print("too old to be a student.")


# def demo():
#     print("没有return的函数")
#     return 123456
#
# n = demo()
#
# print(n)


# name = "miller"
#
#
# def change_name():
#     name = "被编程耽误的 相声演员 miller"
#     print("after change: ", name)
#
#
# change_name()
#
# print("看看外部的name有没有被改变： ", name)


# name = "miller"
#
# def change_name():
#     global name
#     name = "被编程耽误的 相声演员 miller"
#     print("after change: ", name)
#
# change_name()
#
# print("看看外部的name有没有被改变： ", name)


# after change:  被编程耽误的 相声演员 miller
# 看看外部的name有没有被改变：  miller


# after change:  被编程耽误的 相声演员 miller
# 看看外部的name有没有被改变：  被编程耽误的 相声演员 miller


# 1. 函数的外部想要获取函数的执行结果时, 函数内部需要通过return 将执行结果进行返回！ 如果没有return的话， 默认返回None
#   函数内的程序在执行过程中, 遇到return时, 就直接结束。

# 2.在函数中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。

# 3.在函数内想要修改全局变量的时候, 需要通过 global 进行显式的声明.


# li = [0, 1, 2, 3, 4]
#
#
# def change_list():
#     li.append(5)
#     print(li)
#
# change_list()
# print(li)


# d = {"name": "miller", "age": 26, "hobby": "大保健"}
# l = ["Rebeeca", "Katrina", "Rachel"]
#
#
# def change_data():
#     d["hobby"] = "学习"
#     l.append("black_girl")


# change_data()
# print(d, l)

# {'name': 'miller', 'age': 26, 'hobbie': '学习'} ['Rebeeca', 'Katrina', 'Rachel', 'XiaoYun']
# {'name': 'miller', 'age': 26, 'hobby': '学习'} ['Rebeeca', 'Katrina', 'Rachel', 'black_girl']


# name = "miller"
#
# def change_name():
#     name = "liusir"
#     def inner():
#         name = "kevin"
#         print("第三层打印：", name)
#     inner()
#     print("第二层打印：", name)
#
# change_name()
#
# print("第一层打印", name)


# def func():
#     print("这是一个函数")
#
#
# func()


# def calc(x, y):
#     return x ** y
#
# print(calc(2, 3))
#
#
# calc = lambda x, y: x**y
# print(calc(2, 3))

# n = 1
# m = 0
# while n < 101:
#     m += n
#     n+=1
#
# print(m)


# from functools import reduce

# li = list(range(1, 101))
# print(li)
# res = reduce(lambda x,y:x+y, li)
#
# print(res)

# li = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]


#
# new_li = []
# for i in li:
#     new_li.append(i * 2)
#
# print(new_li)

# def calc(x):
#     for i in range(len(x)):
#         x[i] *= 2
#     return x
#
# map(calc, li)
#
#
# def calc():
#     print("calc")
#
#
# xxxx = calc
# xxxx()


# def get_abs(n):
#     if n < 0:
#         n = int(str(n).strip("-"))
#     return n
#
#
# def add(x, y, func):
#     return func(x) + func(y)
#
#
# res = add(3, -6, get_abs)
# print(res)


# print(2*3)




