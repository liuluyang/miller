# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/23 10:18
import os
import pickle
from conf import settings


def get_info():
    if os.path.exists(settings.SCHOOL_INFO_DIR):
        with open(settings.SCHOOL_INFO_DIR, "rb") as f:
            return pickle.loads(f.read())
    else:
        return {}





