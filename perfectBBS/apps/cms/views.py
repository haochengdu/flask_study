#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/15 13:42
@Author  : TX
@File    : views.py
@Software: PyCharm
"""
from flask import Blueprint, render_template

cms_bp = Blueprint('cms_bp', __name__, url_prefix='/cms')


@cms_bp.route('/index')
def index():
    return render_template('cms-index.html')
