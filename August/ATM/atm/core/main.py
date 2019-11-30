# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 15:29

from ..databases import account
from .transaction import all_method


def controller():
    li = []
    for k, v in all_method.items():
        li.append("      %s    %s\n" % (k, v.text))
    while True:
        print("菜单栏".center(40, "-"), "".join(li), "菜单栏".center(40, "-"), sep="\n")
        choice = input("请选择你他吗要干啥:").strip()
        if choice.isdigit() and int(choice) <= len(all_method):
            all_method[choice]()


def identification():
    n = 0
    while n < 3:
        username = input("请输入用户名：")
        pwd = input("请输入密码：")
        user_obj = account.read_info(username)
        if not user_obj:
            print("用户名密码错误")
        elif user_obj["status"] != 0:
            print("账户已锁定, 请联系管理员")
            break
        elif user_obj["data"]["password"] != pwd:
            print("用户名密码错误")
        else:
            controller()
            break
        n += 1

    if n == 3 and user_obj:
        user_obj["data"]["status"] = 1
        account.write_info(username, user_obj["data"])





