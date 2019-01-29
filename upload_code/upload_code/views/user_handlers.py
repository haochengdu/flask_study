#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 11:22
@Author  : TX
@File    : user_handlers.py
@Software: PyCharm
用户相关的一些操作
"""
from flask import Blueprint, render_template, request, session, redirect, url_for
from utils.mysqldb import MySQLHelper
from utils.get_md5 import get_md5

user_handlers = Blueprint('user_handlers', __name__)


@user_handlers.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # post逻辑
    username = request.form.get("user", '').strip()
    pwd = request.form.get("pwd", '').strip()
    # 登录校验
    if all((username, pwd)):
        try:
            # md5加密
            pwd = get_md5(pwd)
            mysql_helper = MySQLHelper()
            sql = 'SELECT id,nickName FROM userInfo WHERE userName=%s AND pwd=%s'
            user = mysql_helper.fetch_one(sql, args=(username, pwd))
            if user:
                session['user_info'] = user
                return redirect('/home')
            return render_template('login.html', message='用户名或密码错误')
        except Exception as e:
            return 'MySQL错误= {}'.format(e)


@user_handlers.route('/logout')
def logout():
    del session['user_info']
    return redirect(url_for('user_handlers.login'))
    














