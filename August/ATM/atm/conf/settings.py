# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 16:21

import os

# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户账户路径
ACCOUNT_FILE_DIR = os.path.join(os.path.join(BASE_DIR, "databases"), "account")

# 日志信息路径
LOG_FILE_BASE_DIR = os.path.join(BASE_DIR, "log")  # 日志基础路径
ASSERT_LOG_DIR = os.path.join(LOG_FILE_BASE_DIR, "access")  # 登录信息日志
ERROR_LOG_DIR = os.path.join(LOG_FILE_BASE_DIR, "error")  # 错误信息日志




