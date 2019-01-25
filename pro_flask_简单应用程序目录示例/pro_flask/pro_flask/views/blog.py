#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

# 创建蓝图
blog = Blueprint('blog', __name__)


@blog.route('/blog_index')
def aaa():
    return 'aaa'

