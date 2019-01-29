#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 11:13
@Author  : TX
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask, request, session, redirect, url_for

from .views.index import up_index
from .views.user_handlers import user_handlers

app = Flask(__name__)
# 添加配置文件
app.config.from_object('configs.settings.DevelopmentConfig')
# 蓝图进行注册
app.register_blueprint(up_index)
app.register_blueprint(user_handlers)


# 全局的before_request装饰器
@app.before_request
def my_login_auth():
    except_path = ['/login', '/favicon.ico']
    if request.path in except_path:
        return None
    if not session.get('user_info', None):
        return redirect(url_for('user_handlers.login'))
    return None
