#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/15 11:46
@Author  : TX
@File    : main.py
@Software: PyCharm
"""
from flask import Flask
from apps.cms import cms_bp


app = Flask(__name__)
# 添加配置文件
app.config.from_object('configs.settings.DevelopmentConfig')
# 蓝图进行注册
app.register_blueprint(cms_bp)


# 全局的before_request装饰器
# @app.before_request
# def my_login_auth():
#     except_path = ['/login', '/favicon.ico']
#     if request.path in except_path:
#         return None
#     if not session.get('user_info', None):
#         return redirect(url_for('user_handlers.login'))
#     return None

if __name__ == '__main__':
    app.run()

