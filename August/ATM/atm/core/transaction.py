# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 16:08


all_method = {}


def wapper(num):
    def inner(func):
        all_method[num] = func
        return func
    return inner


@wapper("1")
def show_info():
    print("展示用户信息")
show_info.text = "展示用户信息"


@wapper("2")
def draw_money():
    print("取款")
draw_money.text = "取款"


@wapper("3")
def transfer_accounts():
    print("转账")
transfer_accounts.text = "转账"


@wapper("4")
def repayment():
    print("还款")
repayment.text = "还款"
