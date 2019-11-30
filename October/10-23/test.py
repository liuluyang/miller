# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 9:02

import time
from threading import Thread


# def sayhi(name):
#     time.sleep(2)
#     print("%s say 'hello'" % name)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=sayhi, args=("miller",))
#     t1.start()
#     print("主线程")


# class MyThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         time.sleep(2)
#         print("%s say 'hello'" % self.name)
#
#
# if __name__ == '__main__':
#     t2 = MyThread("miller")
#     t2.start()
#     print("主线程")


# res = input(">>>")
#
# print(res.upper())
#
#
# with open()
import time


res = None

def recv():
    global res
    res = input(">>>")


# def print_res():
#     while True:
#         if res:
#             print(res)
#             break
#         time.sleep(0.5)
#
#
# def save():
#     while True:
#         if res:
#             with open("./test.txt", "w", encoding="utf-8") as f:
#                 f.write(res)
#             break
#         time.sleep(0.5)


# def print_res():
#     global res
#     res = res.upper()
#     print(res)

# def save():
#     with open("./test.txt", "w", encoding="utf-8") as f:
#         f.write(res)

# if __name__ == '__main__':
#     t1 = Thread(target=recv)
#     t2 = Thread(target=print_res)
#     t3 = Thread(target=save)
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     t3.start()

