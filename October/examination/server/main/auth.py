# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/30 20:17

import configparser
from conf import config

filename = config.ACCOUNT


def authentication(username, pwd):
    conf_obj = configparser.ConfigParser()  # 获取config对象
    conf_obj.read(filename, encoding="utf-8")  # 将内容读取出来
    all_name = conf_obj.sections()  # 获取到所有的 sections 截面
    if username in all_name:
        password = conf_obj.get(username, "pwd")  # get 获取某个截面下的, 某一个option。
        if pwd == password:
            return username


