#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 19-2-1 下午9:39
@Author  : TX
@File    : 面向对像的__new__方法.py
@Software: PyCharm
"""


class Bar(object):
    pass


class Foo(object):
    def __new__(cls, *args, **kwargs):
        return Bar()

foo = Foo()
print(foo)
