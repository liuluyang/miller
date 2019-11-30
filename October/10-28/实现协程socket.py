# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 15:19

from gevent import monkey; monkey.patch_all()
from socket import *
# import gevent

from threading import Thread

# 如果不想用money.patch_all()打补丁,可以用gevent自带的socket
# from gevent import socket
# s=socket.socket()


def server(server_ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((server_ip, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        t = Thread(target=talk, args=(conn, addr))
        t.start()
        # gevent.spawn(talk, conn, addr)


def talk(conn, addr):
    try:
        while True:
            res = conn.recv(1024)
            if not res: break
            print('client %s:%s msg: %s' % (addr[0], addr[1], res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    server('127.0.0.1', 8080)
