# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/8/24 8:56

import time


def timer(name1):
    def outer(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print(name1)
            print(end_time - start_time)
        return inner
    return outer


@timer("miller")
def test_time(name):
    time.sleep(3)
    print("%s睡了三秒" % name)


# test_time("miller1111")


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        '''
        :param cls:  当前准备创建类的对象
        :param name:  当前类的名字
        :param bases: 当前类继承的父类的集合
        :param attrs: 当前类的属性和方法的集合
        :return: 使用type 类生成的一个  元类
        '''
        def add(self, val):
            print(self)
            self.append(val)

        attrs["add"] = add
        return type.__new__(cls, name, bases, attrs)

# class ListMetaclass(type):
#     def __new__(cls, *args, **kwargs):
#         args[2]["add"] = lambda self, val: self.append(val)
#         return type.__new__(cls, *args, **kwargs)


class My_List(list, metaclass=ListMetaclass):
    pass


li = My_List()
li.add(23)
print(li)