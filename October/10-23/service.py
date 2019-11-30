# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 10:29


import socket
from threading import Thread


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 8080))
sk.listen(5)


def get_request():
    while True:
        conn, addr = sk.accept()
        t1 = Thread(target=server, args=(conn, addr))
        t1.start()


def server(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
        except Exception as e:
            print(e)
            break

        data = data.decode()
        print(data)
        data = data.upper()
        conn.send(data.encode())


if __name__ == '__main__':
    get_request()






