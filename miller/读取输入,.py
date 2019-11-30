# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/26 19:02


# def factory(class_name, field_names):
#     try:
#         field_names = field_names.replace(",", " ").split()
#     except Exception as e:
#         pass
#     field_names = tuple(field_names)
#
#     def __init__(self, *args, **kwargs):
#         attrs = dict(zip(self.__slots__, args))
#         attrs.update(kwargs)
#         for name, value in attrs.items():
#             setattr(self, name, value)
#
#     def __iter__(self):
#         for name in self.__slots__:
#             yield getattr(self, name)
#
#     def __repr__(self):
#         values = ",".join("{}={!r}".format(*i) for i in zip(self.__slots__, self))
#         return "{}({})".format(self.__class__.__name__, values)
#
#     class_dic = dict(
#         __slots__=field_names,
#         __init__=__init__,
#         __iter__=__iter__,
#         __repr__=__repr__
#     )
#     return type(class_name, (object,), class_dic)
#
#
# Person = factory("Person", "name age")
#
# p = Person("miller", 26)
#
# print(p)


def factory(class_name, field_names):
    try:
        field_names = field_names.replace(",", "").split()
    except Exception as e:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ",".join("{}={!r}".format(*i) for i in zip(self.__slots__, self))
        return "{}({})".format(self.__class__.__name__, values)

    class_dic = dict(
        __slots__=field_names,  # 将实例属性名, 通过类属性的方式, 添加到类中。
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__
    )

    return type(class_name, (object,), class_dic)


Person = factory("Person", ["name", "age", "salary", "position"])


p = Person("miller", 26, 50, "CEO")














