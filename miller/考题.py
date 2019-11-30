# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/29 8:29


# 1. 简单说明 @property   @staticmethod  @classmethod 的作用
# 1. property  使一个方法, 可以像属性一样去调用
# 2. staticmethod
# 3. classmethod

# class Foo:
#     def xxx(self):
#         return 12345
#
#     @classmethod
#     def abcd(cls):
#         return 54



class A:
    pass


class B:
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


class F(E, D):
    pass


# 2. 写出 F类的, mro列表！
# F E C A D B object


# 3. 新式类 和 经典类, 的区别!


# 4. python中调用 __call__ 方法时，执行了什么?
# 1. 创建空对象
# 2. 初始化对象
# 3. 返回对象
class Meta(type):
    def __call__(self, *args, **kwargs):
        print("创建新对象")
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj


class Person(metaclass=Meta):
    def __init__(self, name):
        self.name = name

# print(p.name)


# 5. Python中类定义的要素
# 1. 类名称
# 2. 类的继承
# 3. 类的名称空间

# pppp = type("Person", (object, ), {"xxxx":lambda x:x*2})


# 6. 以下关于__str__方法和__repr__方法说法正确的是(A B C D).
# A   我们可以使用 __str__ 和 __repr__ 方法定义类到字符串的转化方式
# B   __str__ 的返回结果在于强可读性，而 __repr__ 的返回结果在于准确性。
# C   我们至少需要添加一个 __repr__ 方法来保证类到字符串的自定义转化的有效性，__str__ 是可选的
# D   默认情况下，在需要却找不到 __str__ 方法的时候，会自动调用 __repr__ 方法


# 7. 请说明, 重用父类两种的方式。
# class Human:
#     def __init__(self):
#         pass
#
# class Male(Human):
#     Human.__init__(self)
#     super(Male, self).__init__()

# 8、面向对象中，下列选项中对__new__与__init__的描述正确的是（A B D）。
# A   __new__的第一个占位参数是class对象
# B   __new__ 用来创建实例，在返回的实例上执行__init__，如果不返回实例那么__init__将不会执行
# C   __init__的第一个占位参数是class的实例对象
# D   __init__ 用来初始化实例，为其实例设置属性。


# 9. 类中第一参数 self 代表的是什么？ cls 代表的是什么？


# 10. 简单说说 面向对象 三大特性！


# 11. 使用 logging 模块。 以面向对象的方式。 实现一个单例模式的 logger 对象。 并且可以向文件和屏幕输出。
# 要求： 日志内容 最少包含: 日期 日志级别
import logging
import os


class MyLogger(object):
    __instance = None

    def __init__(self):
        self.run_log = None
        self.error_log = None
        self.run_log_file = r"D:\education_project\miller\run_log"
        self.error_log_file = r"D:\education_project\miller\error_log"
        self.initialize_error_log()
        self.initialize_run_log()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def check_file_path(file_path):
        log_path = os.path.split(file_path)[0]
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    def initialize_run_log(self):
        self.check_file_path(self.run_log_file)
        logger_1_1 = logging.Logger("run_log", level=logging.INFO)  # 获取logger对象
        file_1_1 = logging.FileHandler(self.run_log_file)  # 获取 Handler 对象
        terminal = logging.StreamHandler()

        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s ")  # 获取 Formatter 对象

        file_1_1.setFormatter(fmt=fmt)  # 为 Handler对象，设置 Formatter
        logger_1_1.addHandler(hdlr=file_1_1)  # 为 logger 对象添加, Handler

        terminal.setFormatter(fmt=fmt)
        logger_1_1.addHandler(terminal)

        self.run_log = logger_1_1

    def initialize_error_log(self):
        self.check_file_path(self.error_log_file)
        logger_2_2 = logging.Logger("error_log", level=logging.ERROR)  # 获取logger对象
        file_2_2 = logging.FileHandler(self.error_log_file)  # 获取 Handler 对象
        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s ")  # 获取 Formatter 对象

        file_2_2.setFormatter(fmt=fmt)  # 为 Handler对象，设置 Formatter
        logger_2_2.addHandler(hdlr=file_2_2)  # 为 logger 对象添加, Handler

        self.error_log = logger_2_2

    def log(self, message, mode=True):
        if mode:
            self.run_log.info(message)
        else:
            self.error_log.error(message)


def my_log():
    logger = logging.getLogger('mysql.log')

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    return logger


logger = my_log()

logger.error("asd")
logger.error("asd")
logger.error("asd")


print(logger.handlers)


