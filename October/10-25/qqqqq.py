# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/25 8:56

# from threading import Thread, currentThread
# import queue
# import time
#
#
# def task(q):
#     q.task_done()
#
#
# def work(q):
#     time.sleep(2)
#     q.get()(q)
#     print("job %s is runing " % currentThread().getName())
#
#
# if __name__ == '__main__':
#     q = queue.Queue(10)
#
#     for i in range(10):
#         q.put(task)
#
#     for i in range(9):
#         t = Thread(target=work, args=(q,))
#         t.start()
#
#     q.join()
#
#     print("miller")

# q = queue.LifoQueue()  # 先进后出  栈  stack
#
# q.put("first")
# q.put("second")
# q.put("third")
#
# print(q.get())
# print(q.get())
# print(q.get())


# q = queue.PriorityQueue()
#
# q.put((0.124, "first"))
# q.put((0.025, "second"))
# q.put((30, "third"))
#
# print(q.get())
# print(q.get())
# print(q.get())


# from collections import deque

# q = deque()

# q.append("first")
# q.append("second")

# q.appendleft("third")

# q.insert(2, "444444")

# third first 444444 second

# print(q.pop())
# print(q.pop())
# print(q.popleft())

# print(q.count("first"))

# q.rotate(-1)
# print(q.pop())
# import time
#
# total = 6546845
#
# recved_size = 0
# while recved_size < total:
#     xxsize = total // 50
#     recved_size += 100000
#     num = recved_size // xxsize
#     print("\r[{}{}]{:.1%}".format("=" * num, " " * (50-num), recved_size/total), end="")
#     time.sleep(0.1)

# from queue import Queue, LifoQueue, PriorityQueue









