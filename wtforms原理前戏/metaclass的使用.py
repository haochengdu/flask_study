#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 19-2-1 下午9:56
@Author  : TX
@File    : metaclass的使用.py
@Software: PyCharm
"""


class MyType(type):
    def __init__(cls, *args, **kwargs):
        super(MyType, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Foo(object, metaclass=MyType):
    a1 = 8888

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        pass

    def func(self):
        return 6666

# Foo是MyType类的实例对象
# obj是Foo类的实例对象
obj = Foo()
print(obj)
