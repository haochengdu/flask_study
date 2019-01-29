#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 14:13
@Author  : TX
@File    : get_md5.py
@Software: PyCharm
import hashlib
m = hashlib.md5(b'salt')
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
b'\\xbbd\\x9c\\x83\\xdd\\x1e\\xa5\\xc9\\xd9\\xde\\xc9\\xa1\\x8d\\xf0\\xff\\xe9'
"""
import hashlib

from configs.settings import Config


def get_md5(str_target):
    m = hashlib.md5(bytes(Config.SALT, encoding='utf-8'))
    m.update(bytes(str_target, encoding='utf-8'))
    # secret = m.digest()  # 返回bytes
    secret = m.hexdigest()  # 返回str
    return secret


if __name__ == '__main__':
    print(get_md5('123456'))
