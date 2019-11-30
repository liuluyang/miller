# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/23 14:20


# from threading import Thread, currentThread
# import time
# import random
# #
# #
# # def work():
# #     print("%s runing" % currentThread().getName())
# #     time.sleep(2)
# #     print("%s end" % currentThread().getName())
# #
# #
# # def work1():
# #     print("%s runing" % currentThread().getName())
# #     time.sleep(3)
# #     print("%s end" % currentThread().getName())
# #
# #
# # def work2():
# #     print("%s runing" % currentThread().getName())
# #     time.sleep(4)
# #     print("%s end" % currentThread().getName())
# #
# #
# # if __name__ == '__main__':
# #     t1 = Thread(target=work)
# #     t2 = Thread(target=work1)
# #     t3 = Thread(target=work2)
# #
# #     # t1.daemon = True
# #     t2.daemon = True
# #     t3.daemon = True
# #
# #     t1.start()
# #     t2.start()
# #     t3.start()
# #
# #     print("主线程")
#
#
#
#
#
# # Thread-1 runing
# # Thread-2 runing
# # Thread-3 runing
# #
# # 主线程
# #
# # Thread-1 end
# # Thread-2 end
# # Thread-3 end
#
#
#
# def sayhi(name):
#     time.sleep(2)
#     print("%s say hello" % name)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=sayhi, args=("miller",))
#     t1.setDaemon(True)
#     t1.start()
#
#     print("主线程")
#     time.sleep(3)
#     print(t1.isAlive())


# from threading import Thread
# import time
#
# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")

# if __name__ == '__main__':
#     t1 = Thread(target=foo)
#     t2 = Thread(target=bar)
#
#     # t1.daemon = True
#     t2.daemon = True
#
#     t1.start()
#
#     t2.start()
#
#     print("main-------")
