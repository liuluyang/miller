#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/15 8:35
# 练习题1 —— 全局替换程序：
# sys.argv()
# 写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
# python your_script.py old_str new_str filename
# 替换完毕后打印替换了多少处内容
# import sys
# import os
#
# def inp():
#     res = sys.argv
#     if len(res) != 4:
#         return None
#     else:
#         _, old_str, new_str, filename = res
#         print("这里打印的",_, old_str, new_str, filename)
#         return old_str, new_str, filename
#
#
# def my_replace(old_str, new_str, filename):
#     new_filename = filename + ".new"
#     print(new_filename)  # staff_data.new
#     with open(filename, "r", encoding="utf-8") as read_f, open(new_filename, "w", encoding="utf-8") as write_f:
#         count = 0
#         for line in read_f:
#             count += line.count(old_str)
#             new_line = line.replace(old_str, new_str)
#             write_f.write(new_line)
#     # staff_data.new  --> staff_data
#     os.replace(new_filename, filename)
#     return count

#     os.remove(filename)  # 删除旧文件
#     os.rename(new_filename, filename)  # 把新文件 更换一个名字

# res = inp()
# print(res)
# if not res:
#     print("参数不对")
# else:
#     old_str, new_str, filename = res
#     num = my_replace(old_str, new_str, filename)


# 作业：
# 1 程序启动后，给用户提供查询接口，允许用户重复查股票行情信息(用到循环)
# 2 允许用户通过模糊查询股票名，比如输入“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
# 3 允许按股票价格、涨跌幅、换手率这几列来筛选信息，
#      比如输入“价格>50”则把价格大于50的股票都打印，输入“市盈率<50“，则把市盈率小于50的股票都打印，不用判断等于。


# stock_data.txt 此文件请从课件中下载。
# 思路提示：加载文件内容到内存，转成dict or list结构，然后对dict or list 进行查询等操作。
# 这样以后就不用每查一次就要打开一次文件了，效率会高。


# def read_info(filename):
#     li = []
#     with open(filename, "r", encoding="utf-8") as f:
#         title = f.readline()
#         for line in f:
#             li.append(line.strip().split(","))
#     return title, li
#
#
# def unify_initialize(title, li):
#     '''
#     :param li:
#     :return:
#     '''
#     result = {}
#     for i in range(len(li)):
#         for j in range(len(li[i])):
#             if li[i][j].endswith("%"):
#                 li[i][j] = li[i][j].replace("%", "")
#             elif li[i][j].endswith("万"):
#                 res = li[i][j].replace("万", "")
#                 li[i][j] = float(res) * 10000
#             elif li[i][j].endswith("亿"):
#                 res = li[i][j].replace("亿", "")
#                 li[i][j] = float(res) * 100000000
#     res = list(zip(*li))
#     for index, val in enumerate(title.split(",")):
#         result[val] = res[index]
#     return result
#
#
# def search_all(search_val, result_dic):
#     res = []
#     curr = "%s %s %s"
#     search, opreation, val = search_val
#     for ind, valuse in enumerate(result_dic[search]):
#         if eval(curr % (valuse, opreation, val)):
#             res.append(ind)
#     return res
#
#
# def print_info(result_dic, all_li, title):
#     li_all = []
#     for ind, tu in enumerate(result_dic.values()):
#         li = []
#         for i in all_li:
#             li.append(tu[i])
#         li_all.append(li)
#
#     info = list(zip(*li_all))
#     print(title, end="")
#     for j in info:
#         print(j)
#
#
# def fuzzy_search(name, result_dic):
#     li = []
#     for ind, val in enumerate(result_dic["名称"]):
#         if name in val:
#             li.append(ind)
#     return li
#
#
# if __name__ == '__main__':
#     title, li = read_info("stock_data.txt")
#     result = unify_initialize(title, li)

#     while True:
#         search_val = None
#         condition = input("请输入查询内容：")
#         if "<=" in condition:
#             search_val = condition.partition("<=")
#         elif ">=" in condition:
#             search_val = condition.partition(">=")
#         elif ">" in condition:
#             search_val = condition.partition(">")
#         elif "<" in condition:
#             search_val = condition.partition("<")
#         elif "==" in condition:
#             search_val = condition.partition("==")
#         elif "!=" in condition:
#             search_val = condition.partition("!=")
#         else:
#             all_li = fuzzy_search(condition, result)
#
#         if search_val:
#             all_li = search_all(search_val, result)
#
#         print_info(result, all_li, title)







