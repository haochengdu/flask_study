#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 19-2-1 下午9:46
@Author  : TX
@File    : 类创建的两种方式.py
@Software: PyCharm
"""


# class Foo(object):
#     a1 = 8888
#     def func(self):
#         return 6666


Foo = type('Foo', (object,), {'a1': 8888, 'func': lambda self: 6666})

foo = Foo()
print(foo.a1)
print(foo.func())


