# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/30 20:15


import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

for i in sys.path:
    print(i)
if __name__ == '__main__':
    from main.server import TcpServer, MyHandler
    obj = TcpServer(("127.0.0.1", 8000), MyHandler, max_works=50)
    obj.executor()




