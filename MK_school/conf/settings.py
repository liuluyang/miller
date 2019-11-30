# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/23 10:18
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DB_DIR = os.path.join(BASE_DIR, "db")  # 数据库路径
SCHOOL_INFO_DIR = os.path.join(BASE_DB_DIR, "school")


ACCOUNT_DIR = os.path.join(BASE_DB_DIR, "account.json")





