# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/27 11:35

import os
import pickle

f = open(r"D:\education_project\MK_school\db\school", "rb")
dic = pickle.loads(f.read())
for i in dic:
    print(i, dic[i])



# {
#     "school":{},
#     "teachers":{},
#     "students":{},
#     "courses":{},
# }











