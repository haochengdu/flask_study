#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 18:24
@Author  : TX
@File    : test.py
@Software: PyCharm
"""
# from upload_code.views.test_path import path_test
# 
# print(path_test())


# import os
#
# os.makedirs('F:\\PythonCode\\flask_study\\upload_code\\dsadasdsa')

with open(r'F:\PythonCode\flask_study\upload_code\files\ffacfdc45adb44efba3be42dbc8607f4\main.py', 'rb') as f:
    # f.readlines()
    for line in f:
        print(line)
    f.close()






