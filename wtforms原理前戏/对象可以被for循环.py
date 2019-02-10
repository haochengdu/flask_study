#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 19-2-1 下午9:12
@Author  : TX
@File    : 对象可以被for循环.py
@Software: PyCharm
"""


class Foo(object):
    def __iter__(self):
        # yield 1
        # yield 2
        # yield 3
        # list、dict、str是可迭代对象，可以使用isinstance()判断一个对象是否为可Iterable对象
        # 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
        # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
        # return ['qq', 'ww', 'aa']  # TypeError: iter() returned non-iterator of type 'list'
        return iter(['qq', 'ww', 'aa'])

    def __str__(self):
        # return ['aa', 33, 'asd']  # TypeError: __str__ returned non-string (type list)
        return 'qwe'


foo = Foo()
print(foo)
for one in foo:
    print(one)
