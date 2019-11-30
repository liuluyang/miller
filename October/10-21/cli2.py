# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/21 14:30

import time
import socket


cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("127.0.0.1", 8000))


def send_recv():
    n = 0
    while n < 20:
        cli.send(bytes("Hello %s %s" % (n, "三号客户端"), encoding="utf-8"))
        data = cli.recv(1024)
        data = data.decode()
        print(data)
        n += 1
        time.sleep(1)


send_recv()




