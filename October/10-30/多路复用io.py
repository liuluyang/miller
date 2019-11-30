# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/30 9:19


# import select
# import socket
#
# server = socket.socket()
# server.bind(("127.0.0.1", 8080))
# server.listen(5)
# server.setblocking(False)
#
# r_list = [server]
# w_list = []
#
# w_data = {}
#
# while True:
#     rl, wl, xl = select.select(r_list, w_list, [], 0.5)
#     for sock in rl:
#         if sock == server:
#             conn, addr = sock.accpet()
#             r_list.append(conn)
#         else:
#             try:
#                 data = sock.recv(1024)
#                 if not data: raise ConnectionError
#                 w_list.append(sock)
#                 w_data[sock] = data.upper()
#             except Exception:
#                 sock.close()
#                 r_list.remove(sock)
#
#     for sock in wl:
#         try:
#             sock.send(w_data[sock])
#         except Exception:
#             sock.close()
#             w_list.remove(sock)

# import selectors
# import socket
#
#
# def read(conn, mask):
#     try:
#         data = conn.recv(1024)
#         if not data:
#             print('closing', conn)
#             selectxxx.unregister(conn)
#             conn.close()
#             return
#         conn.send(data.upper() + b'_SB')
#     except Exception:
#         print('closing', conn)
#         selectxxx.unregister(conn)
#         conn.close()
#
#
# def accept(server_fileobj, mask):
#     conn, addr = server_fileobj.accept()
#     selectxxx.register(conn, selectors.EVENT_READ, read)
#
#
# server = socket.socket()
# server.bind(("127.0.0.1", 8000))
# server.listen(5)
# server.setblocking(False)
# selectxxx = selectors.DefaultSelector()
# selectxxx.register(server, selectors.EVENT_READ, accept)
#
#
# while True:
#     events = selectxxx.select(2)  # 检测所有的fileobj，是否有完成wait data的
#     for sel_obj, mask in events:
#         callback = sel_obj.data  # callback=accpet
#         callback(sel_obj.fileobj, mask)  # accpet(server_fileobj,1)
#


# data = {'server_addr': '127.0.0.1', 'server_port': 8000, 'username': None, 'password': '123456'}
#
# print(all(data.values()))

import struct




num = struct.pack("i", 123456)
print(num)

print(struct.unpack("i", b'@\xe2\x01\x00'))