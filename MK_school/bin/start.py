# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/23 10:22

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # D:\education_project\MK_school


if __name__ == '__main__':
    from core import auth
    auth.authentication()
    # from db import test



