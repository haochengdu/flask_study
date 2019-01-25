#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/24 13:58
@Author  : TX
@File    : cbv_test.py
@Software: PyCharm
"""
import functools
from flask import Flask, views, url_for

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')


def wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('1111111111111111111111')
        return func(*args, **kwargs)

    return inner


class UserView(views.MethodView):
    """
    CBV继承views.MethodView
    """
    # 指定请求方法
    methods = ['GET', 'POST']
    # 指定装饰器，为该类的每一个请求方法都装饰上
    decorators = [wrapper, ]

    def get(self, *args, **kwargs):
        return 'GET'

    def post(self, *args, **kwargs):
        return 'POST'


@app.route('/test_')
def test_():
    url_test = url_for('uuuu')
    return 'dsadasd'

# CBV 不能够使用装饰器来指定路由，第二个函数endpoint一般设置None也可以在as_view中指定
app.add_url_rule('/user', None, UserView.as_view('uuuu'))

if __name__ == '__main__':
    app.run()
