# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/29 14:31

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(("127.0.0.1", 8000))

while True:
    sk.send(input(">>>").encode())
    data = sk.recv(1024)
    print(data.decode())





