#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/21 9:10
@Author  : TX
@File    : settings.py
@Software: PyCharm
flask的配置文件
"""
from datetime import timedelta


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'myflasksecretkey'  # 加密的盐
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # session保存的天数


class ProductionConfig(Config):
    """
    生产时的配置信息
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    开发时的配置信息
    """
    DEBUG = True


class TestingConfig(object):
    """
    测试时的配置信息
    """
    TESTING = True


