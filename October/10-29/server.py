# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/29 14:30


import socket
from threading import Thread

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(("127.0.0.1", 8800))
sk.listen(5)


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            data = data.decode()
            print(data)
            conn.send(data.upper().encode())
        except Exception as e:
            print(e)
            break


while True:
    print("server forever")
    conn, addr = sk.accept()
    t = Thread(target=communicate, args=(conn, ))
    t.start()



