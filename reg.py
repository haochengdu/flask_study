#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/24 14:34
@Author  : TX
@File    : reg.py
@Software: PyCharm
"""
from flask import Flask, url_for

app = Flask(__name__)

# 步骤一：定制类
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        # 加了int指定返回int类型，不指定返回字符串
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val


# 步骤二：添加到转换器
app.url_map.converters['reg'] = RegexConverter

"""
1. 用户发送请求
2. flask内部进行正则匹配
3. 调用to_python(正则匹配的结果)方法
4. to_python方法的返回值会交给视图函数的参数
"""


# 步骤三：使用自定义正则
@app.route('/index/<reg("\d+"):nid>')
def index(nid):
    print(nid, type(nid))

    print(url_for('index', nid=987))
    return "index"


if __name__ == '__main__':
    app.run()
