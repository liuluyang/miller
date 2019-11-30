# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# 2019/10/30 20:41


import socket
from queue import Queue
from threading import Thread
import struct
import json
import configparser
from conf import config
import os


class ThreadServer(object):
    '''使用Queue作为池, 限制登录数量， 并开启线程为用户服务, 也负责回收线程'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, max_works):
        self.q = Queue(max_works)

    def submit(self, handler_class, data):
        if self.q.qsize() < self.q.maxsize:  # 或者也可以时候 q.full 判断是否满了。没满就添加
            t = Thread(target=handler_class, args=data)
            t.start()
            self.q.put(t)
        else:
            return False

    def close(self):
        work_item = self.q.get()
        del work_item


# 一个比较尴尬的问题, 如果使用提前创建的方式, 多余的没有工作的线程会占用空间。


class TcpServer(object):
    '''用于创建服务端socket 并且启动服务。将任务分发到 其他线程'''
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 5

    def __init__(self, server_address, handler_class, max_works=10):
        self.thread_obj = ThreadServer(max_works)
        self.request_handler_class = handler_class
        self.server_sock = socket.socket(self.address_family, self.socket_type)
        try:
            self.server_sock.bind(server_address)
            self.server_sock.listen(self.request_queue_size)
        except Exception:
            self.server_sock.close()
            raise

    def get_request(self):
        return self.server_sock.accept()

    def executor(self):
        print("开始服务 %s %s" % ("127.0.0.1", 8000))
        while True:
            conn, addr = self.get_request()
            print(conn)
            self.thread_obj.submit(self.request_handler_class, (self.thread_obj, conn, addr))


class MyHandler(object):
    def __init__(self, thread_obj, conn, addr):
        self.thread_obj = thread_obj
        self.conn = conn
        self.addr = addr
        self.filename = config.ACCOUNT
        self.account = None
        # self.current_path = None
        self.handler()

    def handler(self):
        '''首先进行验证, 之后功能分发'''
        try:
            while True:
                data = self.conn.recv(4)
                if not data: raise ConnectionError
                head_total_size = self.unpack_head(data)
                head_data = self.conn.recv(head_total_size)
                if not head_data: raise ConnectionError
                head_dict = json.loads(head_data)
                if hasattr(self, head_dict.get("commend")):
                    func = getattr(self, head_dict.get("commend"))
                    func(head_dict)
                else:
                    self.conn.send()
        except Exception as e:
            print(e)
        finally:
            self.thread_obj.close()

    def pack_head(self, data):
        '''打包报头'''
        data = bytes(json.dumps(data), encoding="utf-8")
        head_length = len(data)
        return (struct.pack("i", head_length), data)

    def unpack_head(self, byt_num):
        '''解析报头的'''
        return struct.unpack("i", byt_num)[0]

    def auth(self, head_dict):
        option = head_dict["option"]
        username = option["username"]
        pwd = option["pwd"]
        res = self.authentication(username, pwd)
        obj = Response()
        if res:
            self.send_head(obj)
        else:
            obj.code = 201
            self.send_head(obj)

    def authentication(self, username, pwd):
        conf_obj = configparser.ConfigParser()  # 获取config对象
        conf_obj.read(self.filename, encoding="utf-8")  # 将内容读取出来
        all_name = conf_obj.sections()  # 获取到所有的 sections 截面

        if username in all_name:
            password = conf_obj.get(username, "pwd")  # get 获取某个截面下的, 某一个option。
            if pwd == password:
                self.account = os.path.join(config.BASE, "db", username)
                return True

    def send_head(self, obj):
        '''仅仅发送报头使用'''
        head_length, byt_data = self.pack_head(obj.__dict__)
        self.conn.send(head_length)
        self.conn.send(byt_data)

    def get(self, head_dict):
        filename = head_dict["option"]["filename"]
        finished = head_dict["option"]["finished"]

        filename = os.path.join(self.account, filename)
        stat = os.stat(filename)
        total_size = stat.st_size
        obj = Response()
        obj.response = {"total_size": total_size}
        self.send_head(obj)
        self.send_file(filename, finished)

    def _get(self):
        pass

    def send_file(self, filename, finished):
        with open(filename, "rb") as f:
            f.seek(finished)
            file_data = f.read()
            self.conn.send(file_data)


class Response(object):
    def __init__(self):
        self.code = 200
        self.response = ""

    # def __repr__(self):
    #     return json.dumps(self.__dict__)
    # __str__ = __repr__


'''
{commend:get, option:{username:xxxx, pwd:xxxx}}
{commend:get, option:{filename:xxxx, finished:xxxx}}
'''

'''
{code:200,response:""}  {code:201,response:""} # 验证的
{code:200, response:xxxxx}  {code:201, response:xxxxx} # cd
{code:200, response:{total_size:50505}}  {code:201, response:{total_size:0}}
'''
