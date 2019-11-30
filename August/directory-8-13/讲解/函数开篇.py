#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/13 9:40

# 什么是函数   what
# 为什么使用函数  way
# 怎么使用函数  how


# while True：
#     if cpu利用率 > 90%:
#         #发送邮件提醒
#         连接邮箱服务器
#         发送邮件
#         关闭连接
#     if 硬盘使用空间 > 90%:
#         #发送邮件提醒
#         连接邮箱服务器
#         发送邮件
#         关闭连接
#     if 内存占用 > 80%:
#         #发送邮件提醒
#         连接邮箱服务器
#         发送邮件
#         关闭连接


# ##############################################################
# def 发送邮件(内容)
#     #发送邮件提醒
#     连接邮箱服务器
#     发送邮件
#     关闭连接


# while True：
#     if cpu利用率 > 90%:
#         发送邮件('CPU报警')
#     if 硬盘使用空间 > 90%:
#         发送邮件('硬盘报警')
#     if 内存占用 > 80%:
#         发送邮件('内存报警')

# ########################################################################
# 将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可


# ########################## 无参数的函数 ####################
# def say_hi():
#     print("hello, i'm miller")
#
# res = say_hi()
# print(res)


# # ########################## 有参数的函数 (位置参数) ####################
# def say_hi(name):
#     print("hello, i'm %s" % name)
#
# say_hi("egon")


## 也可以带着参数
# a, b = 5, 8
# c = a ** b
# print(c)


# # ########################### 有参数的函数(位置参数) 并且还有return的 ####################
# 以上代码 换成 以下的函数。
# a, b = 2, 2
#
#
# def calc(x, y):
#     res = x ** y
#     return res
#
#
# c = calc(a, b)
# print(c)


#  ########################## 默认参数 ####################

# 修改前
# def stu_register(name, age, country, course):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#
#
# stu_register("miller", "23", "CH", "Python")
# stu_register("liuser", "18", "CH", "Python")
# stu_register("baifengjie", "16", "CH", "Php")
# stu_register("lihe", "23", "CH", "UI")


# 修改后

# def stu_register(name, age, course, country="CH"):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#
#
# stu_register("miller", "23", "Python")
# stu_register("liuser", "18", "Python")
# stu_register("baifengjie", "16", "Php", country="australian")
# stu_register("lihe", "23", "UI")

# ###########################################################
# def stu_register(name, age, course="Python", country="CH"):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)


# stu_register("miller", "23", country="RS", course="Golang")
# stu_register("liuser", "18", "Python")
# stu_register("baifengjie", "16", country="australian")
# stu_register("lihe", "23")

# ##################### 关键字参数 ##########################

# def stu_register(name, age, course="Python", country="CH"):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)


# stu_register(age=23, name="miller", country="RS", course="Golang")
# stu_register("miller", 23, country="RS", course="Golang")

# 注意，参数优先级顺序是 位置参数>关键参数

# print(eval("[1,2,3]"))


# ####################### 非固定参数 ################################

# def my_sum(*args):
#     n = 0
#     for i in args:
#         n += i
#     print(n)
#
#
# my_sum(1, 1.2, 3, )


# def stu_register(name="miller", age=23, *args, **kwargs):
#     print(name, age, args, kwargs)


# stu_register("miller", 23, "CH", "Male", "dabaojian", sex="male", course="Python")
# stu_register()

# def stu_register(name, age, *args, **kwargs):  # *kwargs 会把多传入的参数变成一个dict形式
#     print(name, age, args, kwargs)


# stu_register("Alex", 22)
#
# stu_register("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")


# ##########################################################

# def print_info(*args, **kwargs):
#     if not kwargs.get("Hobbie"):
#         kwargs["Hobbie"] = "大保健"
#
#     print("--------------信息--------------")
#     for k, v in kwargs.items():
#         print(k,"  ", v)
#
#
# print_info(name="miller", age=23, sex="M")
#
# print_info(name="miller", age=23, sex="M", Hobbie="学习")


# n = [134654]
# res = len(n)
# print(res)

# ########################### 返回值 ########################

# def my_sum(*args):
#     n = 0
#     for i in args:
#         n += i
#     return {"n":n}
#
#
# res = my_sum(1, 2, 3, 4, 5)
#
# print(res)


# def stu_register(name, age, course='PY', country='CN'):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("age:", age)
#     print("国籍:", country)
#     print("课程:", course)
#     if age > 22:
#         return False
#     else:
#         return True


# registriation_status = stu_register("王山炮", 28, course="PY全栈开发", country='JP')
# if registriation_status:
#     print("注册成功")
# else:
#     print("too old to be a student.")


















