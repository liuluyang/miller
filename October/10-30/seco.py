# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/30 10:39


# from socketserver import BaseRequestHandler, ThreadingTCPServer
#
#
# class MyHandler(BaseRequestHandler):
#     def handle(self):
#         print(self.request)
#         data = self.request.recv(1024)
#         print(data.decode())
#
#
# if __name__ == '__main__':
#     ThreadingTCPServer.allow_reuse_address = True
#     tcp_obj = ThreadingTCPServer(("127.0.0.1", 8000), MyHandler)
#
#     tcp_obj.serve_forever(2)

# import socket
# from multiprocessing import Process
#
# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk.bind(("127.0.0.1", 8000))
# sk.listen(5)
#
#
# def communicate(conn):
#     while True:
#         data = conn.recv(1024)
#         print(data)
#
#
# if __name__ == '__main__':
#     while True:
#         conn, addr = sk.accept()
#
#         p = Process(target=communicate, args=(conn,))
#         p1 = Process(target=communicate, args=(conn,))
#
#         p.start()
#         p1.start()


# import socket
#
# sk = socket.socket()
# sk.bind(("127.0.0.1", 8000))
# sk.listen(5)
#
# while True:
#     conn, addr = sk.accept()
#     while True:
#         data = conn.recv(1027)
#         for i in data.decode().split("\r\n\r\n"):
#             print(i)
#         with open("./jd.html", "r", encoding="utf-8") as f:
#             content = f.read()
#         conn.send(("""HTTP://1.1 200 OK\r\n\r\n %s""" % content).encode("utf-8"))
#         break
#     conn.close()
#     break
# sk.close()


# from concurrent import futures
# import time
#
# print(time.monotonic())  # 28341.325  28394.116  28411.947
#
# def work(name):
#     print(name)
#     time.sleep(3)
#     return "xxxxx"
#
#
# def task(res):
#     data = res.result()
#     print(data)
#
#
# executor = futures.ThreadPoolExecutor(3)
# executor.submit(work, "name").add_done_callback(task)
#
# executor.shutdown()
#
# print("zhuxianc")
# # print(obj.result())
#
# obj = executor.map(work, ["miller", "liusir"])
#
# for i in obj:
#     print(i)
