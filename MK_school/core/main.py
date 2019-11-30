# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/27 10:33
import os
import pickle
from conf import settings


class Base(object):
    def save(self, info, path=settings.SCHOOL_INFO_DIR):
        with open(path, "wb") as f:
            info.setdefault(self.types, {}).update({self.name:self})
            f.write(pickle.dumps(info))

    def __repr__(self):
        values = ",".join("{}={}".format(*i) for i in self.__dict__.items())
        return "{}({})".format(self.__class__.__name__, values)


class School(Base):
    types = "school"

    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type
        self.students = []
        self.teachers = []
        self.classes = []
        self.courses = []

    def add_students(self, obj):
        self.students.append(obj)
        self.save(settings.School_DIR)

    def add_teachers(self, obj):
        self.teachers.append(obj)

    def add_classes(self, obj):
        self.classes.append(obj)

    def add_courses(self, obj):
        self.courses.append(obj)


class Classes(Base):
    types = "classes"

    def __init__(self, name, open_time):
        self.name = name
        self.open_time = open_time


class Course(Base):
    types = "courses"

    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price


class Teacher(Base):
    types = "teachers"

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Student(Base):
    types = "students"

    def __init__(self, name, age):
        self.name = name
        self.age = age
