# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/30 10:32

import hashlib


def encrypt(pwd, salt=None):
    md = hashlib.md5(bytes(pwd, encoding="utf-8"))
    if salt:
        md.update(bytes(salt, encoding="utf-8"))
    return md.hexdigest()







