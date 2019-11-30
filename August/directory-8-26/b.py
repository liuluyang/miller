# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/26 14:02

# import a
#
# def say_hi():
#     print("hello")

# say_hi()
#
# a.say_hi()

# ##############################################################
# print(help("modules"))

# ##############################################################

# import a
#
# a.say_hi()

# ##############################################################

# from a import say_hi
#
# say_hi()

# from my_directory.xxxxxxx.aaa import say_hi
#
#
# say_hi()

# from random import randint as
#
# # print(globals())
# print(iii(1, 10))

# import a
# #######################################################################

# r'''D:\education_project\direvtory-8-26\my_directory\my_directory1'''
# r'''D:\education_project\direvtory-8-26'''

# # from my_directory import a
#
# # #######################################################################
#
# import sys
# import os
#
# for i in sys.path:
#     print(i)

# #######################################################################
#
# import requests
#
# url = "http://www.baidu.com"
#
# response = requests.get(url)
# response.encoding = "utf-8"
#
# with open("baidu.html", "w", encoding="utf-8") as f:
#     f.write(response.text)

# from my_directory.xxxxxxx import aaa


# D:\education_project\direvtory-8-26
import os

# #####################################################

# for i in os.listdir("D:\education_project"):  # 只找儿子  不找孙子
#     print(i)

# #####################################################

# os.remove(r"D:\education_project\direvtory-8-26\baidu.html")  # 删除指定文件, 文件不存在会报错

# os.remove(r"D:\education_project\xxx")  # 不能删除 文件夹 / 包

# #####################################################

# os.removedirs(r"D:\education_project\xxx\xxxxxx\xxxxxx\xxxxxxxxxxxx")
# os.removedirs(r"D:\education_project\xxxx\xxxxx")

# #####################################################
# res = os.path.join("D:\education_project", "asxxx.py")
# print(res)

# bo = os.path.isfile(res)  # 判断给出的路径，是否是一个文件
# # print(bo)

# print(os.path.isdir(r"D:\education_project\asxxx.py"))

# #####################################################

# print(os.path.isabs(r"D:\education_project\direvtory-8-26"))

# #####################################################

# print(os.path.exists(r"D:\education_project\as.py"))  # 检查文件或者文件夹 是否存在

# #####################################################

# print(os.path.split(r"D:\education_project\as.py"))


# print(tuple(r"D:\education_project\as.py".rsplit("\\", 1)))

# #####################################################


# print(os.path.splitext(r"D:\education_project\as.py"))

# print(r"D:\education_project\as.py".partition("."))

# #####################################################
# os.path.abspath(__file__)  # D:\education_project\direvtory-8-26\b.py

# print(os.path.dirname(os.path.abspath(__file__)))  # D:\education_project\direvtory-8-26

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # D:\education_project

# import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# #####################################################

# print(os.path.basename(r"D:\education_project\direvtory-8-26\b.py"))

# #####################################################

# os.system("shutdown -a")

# #####################################################


# print(os.getenv("home"))  # 读取home值

# #####################################################

# print(os.environ)

# os.environ.setdefault('HOME', '/home/alex')
# #####################################################
# res = os.linesep
# print(res.encode("utf-8"))

# #####################################################

# print(os.name)  # nt

# #####################################################

# os.rename(r"D:\education_project\110", r"D:\education_project\120")  # 改名字

# #####################################################

# import time
# os.makedirs(r"D:\xxx\xxx\xxxx\xxx")
# time.sleep(3)
# os.removedirs(r"D:\xxx\xxx\xxxx\xxx")

# #####################################################
# os.mkdir(r"D:\education_project\xxxxxxxx")
# os.removedirs(r"D:\education_project\xxxxxxxx")

# #####################################################

# print(os.stat(r"D:\education_project\test.py"))


# for i in dict(os.stat(r"D:\education_project\test.py")).items():
#     print(i)

# import time
# print(time.strftime("%Y-%m-%d %X", time.localtime(1565682627)))

# os.chmod(r"D:\education_project\test.py", 110)

# #####################################################
# import my_directory.xxxxxxx.aaa
# D:\education_project\directory-8-26
# os.chdir(r"D:\education_project\directory-8-9")

# print(os.getcwd())

# #####################################################
# print(os.path.getsize(r"D:\education_project\test.py"))  # 2141

# #####################################################
# import signal
# os.kill(5200, 9)






