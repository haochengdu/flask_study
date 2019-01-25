#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/22 9:09
@Author  : TX
@File    : hello2.py
@Software: PyCharm
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')


class MyMiddleware(object):
    """
    中间件
    :return:
    """
    def __init__(self, old):
        self.old = old

    def __call__(self, *args, **kwargs):
        # print('11111111111111111111')
        result = self.old(*args, **kwargs)
        # print('2222222222222222222')
        return result


@app.route('/index')
def index():
    return "Index"


if __name__ == '__main__':
    # 此处app.wsgi_app是一个地址作为参数传递，执行result = self.old(*args, **kwargs)时候
    # 其实是跳转到Flask类实例化的app对象中执行wsgi_app方法
    app.wsgi_app = MyMiddleware(app.wsgi_app)
    app.run()






