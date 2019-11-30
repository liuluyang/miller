# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/29 14:58


# import socket
# from threading import Thread
# import time
#
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.bind(("127.0.0.1", 8800))
# sk.listen(5)
# sk.setblocking(False)
#
#
# def communicate(conn):
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data: break
#             data = data.decode()
#             print(data)
#             conn.send(data.upper().encode())
#         except Exception as e:
#             time.sleep(2)
#
#
# while True:
#     print("server forever")
#     try:
#         conn, addr = sk.accept()
#         t = Thread(target=communicate, args=(conn, ))
#         t.start()
#     except BlockingIOError as e:
#         time.sleep(2)


import socket

server = socket.socket()
server.bind(("127.0.0.1", 8090))
server.listen(5)
server.setblocking(False)

r_list = []
w_list = []

while True:
    try:
        conn, addr = server.accept()
        r_list.append(conn)
    except BlockingIOError:
        del_list = []
        for sock in r_list:
            try:
                data = sock.recv(1024)
                if not data: raise ConnectionError
                print(data.decode())
                w_list.append((sock, data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                sock.close()
                del_list.append(sock)

        del_w_list = []
        for item in w_list:
            try:
                item[0].send(item[1])
                del_w_list.append(item)
            except Exception:
                del_w_list.append(item)

        for i in del_list:
            r_list.remove(i)

        for i in del_w_list:
            w_list.remove(i)

















