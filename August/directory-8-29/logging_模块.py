# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/29 13:58

import logging

# logging.warning("user miller.json attempt wrong password more than 3 times")
# logging.error("user miller.json mei qian le ")
# logging.critical("server down")


# debug info warning error critical

# ###########################如何将日志写到文件中########################################

# logging.basicConfig(level=logging.DEBUG)  # level用于 设置日志的输出级别。
# logging.debug("123456789")


# logging.basicConfig(filename="log.log", level=logging.WARNING)
# logging.warning("user miller.json attempt wrong password more than 3 times")
# logging.info("user miller.json login")
# logging.debug("buy chongqiwawa")

# ###########################如何将日志写到文件中 和 format格式########################################

# my_format = "%(levelname)s %(asctime)s %(message)s %(filename)s %(funcName)s %(lineno)s"
#
#
# def xxxx():
#     logging.basicConfig(filename="log.log", format=my_format)  # datefmt 指定日期的显示格式  datefmt="%Y-%m-%d %X %p"
#     logging.warning("user miller.json attempt wrong password more than 3 times")
#     logging.critical("server down")
# xxxx()


# logging.warning("user miller.json attempt wrong password more than 3 times")
# logging.critical("server down")

# ################################ 同时 向文件和屏幕 输出日志 ##########################

# # 1. 获取到一个logger对象
# logger = logging.getLogger("Mysql_log")
#
# # 2. 搞两个handler 一个输出到屏幕 一个输出到文件
#
# ch = logging.StreamHandler()  # 向屏幕输出的
# fh = logging.FileHandler(filename="./log.log")  # 向文件输出的
#
# # 3. 搞两个formatter对象，控制输出的内容
#
# ch_format = logging.Formatter("%(levelname)s %(message)s")
# fh_format = logging.Formatter("%(levelname)s %(asctime)s %(message)s %(filename)s %(funcName)s %(lineno)s")
#
# # 4. 将这个 formatter对象， 绑定到 handler 对象
# ch.setLevel(logging.WARNING)
# fh.setLevel(logging.DEBUG)
#
# ch.setFormatter(ch_format)
# fh.setFormatter(fh_format)
#
# # 5. 将handler对象， 添加到logger对象
# logger.addHandler(ch)
# logger.addHandler(fh)



# 6。 你可以使用logger对象，写快乐的日志了
# try:
#     asdasd
# except Exception as e:
#     logger.warning(e)

def logger(channel):
    filename = channel + ".log"
    logger = logging.getLogger(channel)  # 为避免输出的是同一个logger对象, 这里使用不同的名字进行创建logger对象

    ch = logging.StreamHandler()  # 向屏幕输出的
    fh = logging.FileHandler(filename=filename)  # 向错误日志文件输出的

    ch_format = logging.Formatter("%(levelname)s %(message)s")
    fh_format = logging.Formatter("%(levelname)s %(asctime)s %(message)s %(filename)s %(funcName)s %(lineno)s")
    ch.setLevel(logging.WARNING)
    fh.setLevel(logging.DEBUG)
    ch.setFormatter(ch_format)
    fh.setFormatter(fh_format)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger


# run_logger = logger("run")
# error_logger = logger("error")

# error_logger.error("第一次error")
# error_logger.error("第二次error")
# error_logger.error("第三次error")

# run_logger.error("第一次run")
# run_logger.error("第二次run")
# run_logger.error("第三次run")

# logger("run").error("第一次run")
# logger("run").error("第二次run")
# logger("run").error("第三次run")

# logger("error").error("第一次run")
# logger("error").error("第二次run")
# logger("error").error("第三次run")
