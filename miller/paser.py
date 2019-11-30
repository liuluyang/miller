# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/30 10:21


import re


with open("./movie.html", "r", encoding="utf8") as f:
    movie_str = f.read()
    res = re.findall('''<a href="(https://movie\.douban\.com/subject/\d+/)" class="">
                        (.+?)
                        / <span style="font-size:13px;">.+?</span>
                    </a>''', movie_str)
    print(res)




