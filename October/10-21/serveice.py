# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/21 14:22


import socket
from multiprocessing import Process

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 8000))
sk.listen(10)


def server(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        data = data.decode("utf-8")
        print(data)
        conn.send(data.upper().encode())


if __name__ == '__main__':
    while True:
        conn, addr = sk.accept()
        p = Process(target=server, args=(conn,))
        p.start()




