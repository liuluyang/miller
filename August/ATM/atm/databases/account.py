# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 15:32


import os
import json
from ..conf import settings

def read_info(username):
    file_path = os.path.join(settings.ACCOUNT_FILE_DIR, username + ".json")
    if not os.path.exists(file_path):
        return False
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            user_obj = json.loads(f.read())
            return {"status": user_obj["status"], "data": user_obj}


def write_info(username, user_info):
    file_path = os.path.join(settings.ACCOUNT_FILE_DIR, username + ".json")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(user_info))