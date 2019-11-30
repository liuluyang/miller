# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/30 21:55


import socket
import optparse
import json
import struct
import os


class Client(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option("-s", "--host", dest="host", help="please enter server host addr")
        self.parser.add_option("-P", "--port", dest="port", help="please enter server port", type=int)
        self.parser.add_option("-u", "--username", dest="username", help="please enter you username")
        self.parser.add_option("-p", "--password", dest="pwd", help="please enter you password")
        self.current_pwd = None
        self.download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_file")

    def executor(self):
        options, args = self.parser.parse_args()
        self.parser_data = options.__dict__
        self.current_pwd = self.parser_data["username"]
        if not all(self.parser_data.values()):
            self.parser.print_help()
        else:
            self.connect((self.parser_data.pop("host"), self.parser_data.pop("port")))

    def connect(self, server_addr):
        self.client = socket.socket()
        self.client.connect(server_addr)
        self.auth()

    def auth(self):
        request_obj = Request("auth", self.parser_data)
        head_length, byt_data = self.pack_head(request_obj.__dict__)
        self.client.send(head_length)
        self.client.send(byt_data)
        byt_num = self.client.recv(4)
        head_total_size = self.unpack_head(byt_num)
        head_data = self.client.recv(head_total_size)

        head_dict = json.loads(head_data)
        if head_dict["code"] == 200:
            print("welcome login")
            self.operator()
        else:
            exit("用户名密码错误")

    def pack_head(self, data):
        '''打包报头'''
        data = bytes(json.dumps(data), encoding="utf-8")
        head_length = len(data)
        return (struct.pack("i", head_length), data)

    def unpack_head(self, byt_num):
        '''解析报头的'''
        return struct.unpack("i", byt_num)[0]

    def operator(self):
        msg = '''
        get   下载, get maliya.av
        '''
        while True:
            choice = input("\n[%s]$ " % self.current_pwd)
            option_list = choice.split(" ")
            if hasattr(self, option_list[0]):
                getattr(self, option_list[0])(option_list)
            else:
                print(msg)

    def get(self, option_list):
        if len(option_list) > 1:
            filename = option_list[1]
            unfinished_download = filename + ".download"
        else:
            return

        file_path = os.path.join(self.download_path, unfinished_download)
        if os.path.exists(file_path):
            finished = os.stat(file_path).st_size
            obj = Request(commend=option_list[0], option={"filename": filename, "finished": finished})
            data_length, byt_data = self.pack_head(obj.__dict__)
            self.client.send(data_length)
            self.client.send(byt_data)
            head_length = self.client.recv(4)
            head_length = self.unpack_head(head_length)
            head_dict = self.client.recv(head_length)
            head_dict = head_dict.decode()
            head_dict = json.loads(head_dict)
            self.write_file(file_path, "wb", head_dict, finished)
        else:
            obj = Request(commend=option_list[0], option={"filename": filename, "finished": 0})
            data_length, byt_data = self.pack_head(obj.__dict__)
            self.client.send(data_length)
            self.client.send(byt_data)
            head_length = self.client.recv(4)
            head_length = self.unpack_head(head_length)
            head_dict = self.client.recv(head_length)
            head_dict = head_dict.decode()
            head_dict = json.loads(head_dict)
            self.write_file(file_path, "wb", head_dict)

    def write_file(self, file_path, mode, head_dict, finished_size=0):
        total_size = head_dict["response"]["total_size"]
        gen = self.progress_bar(total_size, finished_size)
        next(gen)
        with open(file_path, mode=mode) as f:
            try:
                while total_size > 0:
                    data = self.client.recv(min(total_size, 4096))
                    f.write(data)
                    total_size -= len(data)
                    gen.send(len(data))
            except StopIteration:
                pass
        os.replace(file_path,
                   os.path.join(os.path.split(file_path)[0], os.path.split(file_path)[1].replace(".download", "")))

    def progress_bar(self, total, finished_size):
        current = finished_size
        while current < total:
            cur_size = yield
            current += cur_size
            num = int(current / total * 100)
            cur_plan = "=" * num
            kong_plan = " " * (100 - num)
            print("\r[{}{}]{:.1%}".format(cur_plan, kong_plan, current / total), end="")


class Request(object):
    def __init__(self, commend, option=""):
        self.commend = commend
        self.option = option


c = Client()
c.executor()
