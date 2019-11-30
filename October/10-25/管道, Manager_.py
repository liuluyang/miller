#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/9/24


from multiprocessing import Process, Pipe, Manager


def sub(conn):
    conn.send([12, {"name": "yuan"}, "hello"])
    response = conn.recv()
    print("response:", response)
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p = Process(target=sub, args=(child_conn, ))
    p.start()
    print(parent_conn.recv())

    parent_conn.send("儿子你好!")
    parent_conn.close()
    p.join()

# 队列和 管道, 也仅仅是实现了, 进程间的通信. 只是实现了数据的交互, 但是并没有实现数据的共享,
# 即一个进程去修改另一个进程的数据


'''---------------------Manager------------------'''
# Manager上下文管理器, 就可以实现不同进程之间共享同一个数据,
# 支持的类型有， list dict Namespace Lock Rlock Semaphore BoundedSemaphore Condition Event
# Barrier Queue  Value Array


# def f(d, l, n):
#     d[n] = "1"
#     d["2"] = 2
#     d[0.25] = None
#     l.append(n)
#
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(5))
#
#         print("main process:", id(d), id(l))
#         p_list = []
#
#         for i in range(10):
#             p = Process(target=f, args=(d, l, i))
#             p.start()
#             p_list.append(p)
#
#         for res in p_list:
#             res.join()
#
#         print(d)
#         print(l)



