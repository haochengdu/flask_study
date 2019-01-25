#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/22 9:29
@Author  : TX
@File    : test.py
@Software: PyCharm
"""


# class MyTest(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print(args)  # ()
#         print(kwargs)  # {}
#         print("__call__")
#         return "aaaa"
#
#     def __str__(self):
#         return "123"
#
#
# if __name__ == '__main__':
#     obj = MyTest("hehe")
#     a = obj
#     # b = obj(123, 333, age=22, addre='beijing')
#     b = obj.__call__(123, 333, age=22, addre='beijing')
#
#     print("------------")

# import threading
# from threading import local
# import time
#
# obj = local()
#
#
# def task(i):
#     obj.xxxxx = i
#     time.sleep(2)
#     print(obj.xxxxx, i)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()


# import time
# import threading
#
# DIC = {}
#
#
# def task(i):
#     ident = threading.get_ident()
#     if ident in DIC:
#         DIC[ident]['xxxxx'] = i
#     else:
#         DIC[ident] = {'xxxxx': i}
#     time.sleep(2)
#
#     print(DIC[ident]['xxxxx'], i)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()


# import time
# import threading
# import greenlet
#
# DIC = {}
#
#
# def task(i):
#     # ident = threading.get_ident()
#     ident = greenlet.getcurrent()
#     if ident in DIC:
#         DIC[ident]['xxxxx'] = i
#     else:
#         DIC[ident] = {'xxxxx': i}
#     time.sleep(2)
#
#     print(DIC[ident]['xxxxx'], i)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()


# import time
# import threading
#
# try:
#     import greenlet
#
#     get_ident = greenlet.getcurrent
# except Exception as e:
#     get_ident = threading.get_ident
#
#
# class My_Local(object):
#     DIC = {}
#
#     def __getattr__(self, item):
#         ident = get_ident()
#         if ident in self.DIC:
#             return self.DIC[ident].get(item)
#         return None
#
#     def __setattr__(self, key, value):
#         ident = get_ident()
#         if ident in self.DIC:
#             self.DIC[ident][key] = value
#         else:
#             self.DIC[ident] = {key: value}
#
#
# obj = My_Local()
#
#
# def task(i):
#     obj.xxxxx = i
#     time.sleep(2)
#     print(obj.xxxxx, i)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()


# import functools
#
#
# def index(a1, a2):
#     return a1 + a2
#
#
# # 原来的调用方式
# # ret = index(1,23)
# # print(ret)
#
# # 偏函数，帮助开发者自动传递参数
# new_func = functools.partial(index, 666)
# ret = new_func(1)
# print(ret)

class MyStack(object):

    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]


my_stack = MyStack()
for i in range(10):
    my_stack.push(i)

my_stack.pop()
my_stack.pop()
my_stack.top()
my_stack.top()

