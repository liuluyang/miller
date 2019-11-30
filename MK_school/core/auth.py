# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/27 9:56
import json
from conf import settings
from core import views


def authentication():
    with open(settings.ACCOUNT_DIR, "r", encoding="utf-8") as f:
        all_user_info = json.loads(f.read())
    while True:
        username = input("请输入用户名:").strip()
        pwd = input("请输入密码:").strip()
        if username not in all_user_info or pwd != all_user_info[username]["pwd"]:
            print("username  or  password is wrong")
            continue
        if hasattr(views, all_user_info[username]["identity"]):
            view = getattr(views, all_user_info[username]["identity"])()
            while True:
                view.handler()
