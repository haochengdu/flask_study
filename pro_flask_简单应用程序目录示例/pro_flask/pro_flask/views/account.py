#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request
# 创建蓝图
account = Blueprint('account', __name__)


@account.route('/login.html', methods=['GET', "POST"])
def login():
    return render_template('login.html')
