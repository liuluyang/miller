# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/28 13:53


# import queue
# from threading import Thread, currentThread
#
#
# def work(name):
#     print("miller  %s"% name, currentThread().getName())
#
#
# if __name__ == '__main__':
#     q = queue.Queue(10)
#     for i in range(10):
#         q.put(Thread(target=work, args=("xxxxxx",)))
#
#     thread_obj = q.get()
#
#     # thread_obj._target = work
#     # thread_obj._args = ("liusir",)
#
#     thread_obj.start()
#     ...
#     ...
#     ...
#     ...
#
#     q.put(thread_obj)

