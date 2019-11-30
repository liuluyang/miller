#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/13


class Description(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        def inner(*args, **kwargs):
            self.func(instance, *args, **kwargs)
        return inner


class Foo(object):
    @Description
    def func(self):
        print("asdhkasdhf")


f = Foo()



