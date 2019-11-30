# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/29 10:39

# from multiprocessing import Process, Queue
# import time, random
#
#
# def producer(q, name, food):
#     for i in range(20):
#         time.sleep(1)
#         res = "第%s个%s" % (i, food)
#         print("%s 生产了 %s " % (name, res))
#         q.put(res)
#
#
# def consumer(q, name):
#     while True:
#         res = q.get()
#         if res is None: break
#         time.sleep(random.randint(1, 2))
#         print("\t\t\t%s 吃了 %s" % (name, res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#
#     p1 = Process(target=producer, args=(q, "alex", "包子"))
#     p2 = Process(target=producer, args=(q, "egon", "泔水"))
#     p3 = Process(target=producer, args=(q, "ritian", "奥利给"))
#
#     c1 = Process(target=consumer, args=(q, "yuan"))
#     c2 = Process(target=consumer, args=(q, "j.sky"))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#
#     q.put(None)
#     q.put(None)


# from multiprocessing import Process, JoinableQueue,Pool
# import time, random
#
#
# def producer(q, name, food):
#     for i in range(10):
#         time.sleep(1)
#         res = "第%s个%s" % (i, food)
#         print("%s 生产了 %s " % (name, res))
#         q.put(res)
#     q.join()
#
#
# def consumer(q, name):
#     while True:
#         res = q.get()
#         time.sleep(1)
#         print("\t\t\t%s 吃了 %s" % (name, res))
#         q.task_done()
#
#
# if __name__ == '__main__':
#     q = JoinableQueue()
#
#     p1 = Process(target=producer, args=(q, "alex", "包子"))
#     p2 = Process(target=producer, args=(q, "egon", "泔水"))
#     p3 = Process(target=producer, args=(q, "ritian", "奥利给"))
#
#     c1 = Process(target=consumer, args=(q, "yuan"))
#     c2 = Process(target=consumer, args=(q, "j.sky"))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.daemon = True
#     c2.daemon = True
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()


# from multiprocessing import Process, Pool
# import time, random


# def work(name):
#     print("%s is runing" % name)
#     return {"name": name}
#
#
# def call_back(res):
#     print("from call_back:", res)


# if __name__ == '__main__':
#     pool = Pool(processes=2)
    # for i in range(10):
    # res = pool.apply_async(work, args=("miller",), callback=call_back)
    # res = pool.map_async(work, iterable=["miller", "liusir"], callback=call_back)
    # pool.apply(work, args=("miller",))

    # print(res.get())



# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, Future

# def work(name):
#     print(name)
#     return "xxxxxx"

# def fun(res):
#     name = res.result()
#     print(name)

# with ThreadPoolExecutor(50) as executor:
#     executor.submit(donwload_one, "miller").add_done_callback(fun)



