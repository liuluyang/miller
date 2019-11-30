# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/31 8:47


# import optparse
# import socket
# import json
# import struct
#
#
# class Client(object):
#     def __init__(self):
#         self.parser = optparse.OptionParser()
#         self.parser.add_option("-s", "--server", dest="server_addr", help="please enter host server addr:: 127.0.0.1")
#         self.parser.add_option("-P", "--port", dest="server_port", help="please enter host server port", type=int)
#         self.parser.add_option("-u", "--username", dest="username", help="please enter your username")
#         self.parser.add_option("-p", "--password", dest="password", help="please enter your password")
#
#     def get_parser(self):
#         options, args = self.parser.parse_args()
#         data = options.__dict__
#         if all(data.values()):
#             addr = data.pop("server_addr")
#             port = data.pop("server_port")
#             self.connect((addr, port), data)
#
#     def connect(self, addr, user_info):
#         self.sk = socket.socket()
#         self.sk.connect(addr)
#         data = json.dumps(user_info).encode()
#
#         pack, b_str = self.pack_head("auth", len(data))
#         self.sk.send(pack)
#         self.sk.send(b_str)
#
#         total_data_size = self.sk.recv(4)
#         num = self.unpack_head(total_data_size)[0]
#
#     def recv_file(self, filesize, recv_size):
#
#         total_size = filesize
#         while total_size > 0:
#             data = self.sk.recv(min(total_size, 1024))
#             total_size -= len(data)
#
#     def pack_head(self, commend, num, *args):
#         dic = {"commend": commend, "size": num, "msg": args}
#         b_str = json.dumps(dic).encode()
#         return (struct.pack("i", len(b_str)), b_str)
#
#     def unpack_head(self, bytes_num):
#         return struct.unpack("i", bytes_num)




import os

# filename = r"""D:\education_project\October\examination\server\start.py.download"""
# filename = r"""D:\education_project\October\examination\server\start.py"""

# print(os.path.exists(filename))

# print(os.path.split(filename))
# ('D:\\education_project\\October\\examination\\server', 'start.py')


