#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/6

# 练习题1 —— 全局替换程序：

# 写几行代码，可以对指定文件内容进行全局替换
# 替换完毕后打印替换了多少处内容



# import sys
# import os
#
# py_name, old_str, new_str, filename = sys.argv
#
# new_filename = filename + ".new"
# f = open(filename, 'r', encoding='utf-8')
# f_new = open(new_filename, "w", encoding="utf-8")
# for line in f:
#     if old_str in line:
#         new_line = line.replace(old_str, new_str)   # sexy_girl   石家庄   171   52   123456
#     else:
#         new_line = line
#     f_new.write(new_line)
# f.close()
# f_new.close()
#
#
# os.replace(new_filename, filename)


# 练习题2 —— 模拟登陆：  (evel 的使用)
# 用户输入帐号密码进行登陆
# 用户信息保存在文件内
# 用户密码输入错误三次后锁定用户，下次再登录，检测到是这个用户也登录不了
# {"miller":{"username":"miller", "pwd":123456, "attempt":0}, "liuser":{"username":"liuser", "pwd":123456, "attempt":0}}
# import os
#
# f = open("./login_test", "r", encoding="utf-8")
# f_new = open("./login.txt", "w", encoding="utf-8")
#
# data = eval(f.read())
#
# num = 0
#
# while num < 3:
#     username = input("请输入用户名: ")
#     pwd = input("请输入密码: ")
#
#     if username not in data:
#         print("username or password wrong")
#         break
#     if data[username]["attempt"] >= 3:
#         print("今天不能登陆了")
#         break
#     else:
#         if data[username]["pwd"] == pwd:
#             print("wellcome %s" % username)
#         else:
#             print("username or password wrong")
#             data[username]["attempt"] += 1
#     num += 1
#
# f_new.write(str(data))
#
# f_name = f.name
# f_new_name = f_new.name
#
# f_new.close()
# f.close()
#
# os.replace(f_new_name, f_name)


# 作业一：双色球选购
# 1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 2 确保用户不能重复选择，不能超出范围
# 3 用户输入有误时有相应的错误提示
# 4 最后展示用户选择的双色球的号码

# lottery station


# red_ball = []
# bull_ball = []
#
# print("\033[1;35m wellcome to mk lottery station\033[0m")
#
# while True:
#     if len(red_ball) < 6:
#         num = int(input("\033[1;31m[%s]Select Red Ball:\033[0m" % (len(red_ball) + 1)))
#         if num < 1 or num > 32:
#             print("only can select between 1 - 32")
#         if num in red_ball:
#             print("number %d is already exist in red ball list" % num)
#         else:
#             red_ball.append(num)
#     elif len(bull_ball) < 2 and len(red_ball) == 6:
#         num = int(input("\033[1;34m[%s]Select Bull Ball:\033[0m" % (len(bull_ball) + 1)))
#         if num < 1 or num > 16:
#             print("only can select between 1 - 16")
#         if num in bull_ball:
#             print("number %d is already exist in bull ball list" % num)
#         else:
#             bull_ball.append(num)
#     elif len(red_ball) == 6 and len(bull_ball) == 2:
#         print(red_ball, "\n", bull_ball, "\n", "Good Luck")
#         break


# 作业二： 数据结构：

# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车站': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }

# 需求：
# 可依次选择进入各子菜单
# 可从任意一层往回退到上一层
# 可从任意一层退出程序
# 所需新知识点：列表、字典
# 作业效果展示：

# last_menu = []
# current_menu = menu
# while True:
#     for key in current_menu:
#         print(key)
#     choice = input("please select next:").strip()
#     if not choice: continue
#     if choice in current_menu:
#         last_menu.append(current_menu)
#         current_menu = current_menu[choice]
#     if choice == "q":
#         if last_menu:
#             current_menu = last_menu.pop()
#         else:
#             print("已经是最顶层")
#     if choice == "Q":
#         current_menu = menu


# 作业三：
# 1 程序启动后，给用户提供查询接口，允许用户重复查股票行情信息(用到循环)
# 2 允许用户通过模糊查询股票名，比如输入“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
# 3 允许按股票价格、涨跌幅、换手率这几列来筛选信息，
#      比如输入“价格>50”则把价格大于50的股票都打印，输入“市盈率<50“，则把市盈率小于50的股票都打印，不用判断等于。

# stock_data.txt 此文件请从课件中下载。
# 思路提示：加载文件内容到内存，转成dict or list结构，然后对dict or list 进行查询等操作。 这样以后就不用每查一次就要打开一次文件了，效率会高。

# data_list = []
#
# with open("stock_data", "r", encoding="utf-8") as f:
#     title = f.readline().split()
#     data_list_new = [[] for _ in title]
#
#     for line in f:
#         line_list = line.split()
#         data_list.append(line_list)
#         for index, val in enumerate(line_list):
#             data_list_new[index].append(val)
#
# data_dict = dict(zip(title, data_list_new))


# while True:
#     result_num = 0
#     text = input('输入查询内容:')
#     print(title)
#     params = []
#     for symbol in ['<', '>']:
#         if symbol in text:
#             params = text.split(symbol)
#             params.append(symbol)
#     if params:
#         if params[-1] == '<':
#             for index, name in enumerate(data_dict.get(params[0].strip())):
#                 if float(name) < float(params[1]):
#                     result_num += 1
#                     print(data_list[index])
#         elif params[-1] == '>':
#             for index, name in enumerate(data_dict.get(params[0].strip())):
#                 if float(name) > float(params[1]):
#                     result_num += 1
#                     print(data_list[index])
#     else:
#         for index, name in enumerate(data_dict.get('名称')):
#             if text in name:
#                 result_num += 1
#                 print(data_list[index])
#     print('找到%s条'%(result_num))
#
