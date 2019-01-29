#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 14:36
@Author  : TX
@File    : mysqldb.py
@Software: PyCharm
对MySQL数据的简单操作
"""
import pymysql

from configs.settings import Config


class MySQLHelper(object):

    # def __init__(self):
    #     # 连接数据库
    #     # conn = pymysql.connect("192.168.2.223", "root", "oldboy", "upload_code_flask")  # 查询返回元组
    #     conn = pymysql.connect(
    #         host="192.168.2.223",
    #         user="root",
    #         passwd="oldboy",
    #         db="upload_code_flask",
    #         port=3306,
    #         charset='utf8',
    #         cursorclass=pymysql.cursors.DictCursor
    #     )
    #     self.mysql_conn = conn
    #     # 使用cursor()方法创建一个游标对象
    #     self.cursor = db.cursor()
    def __init__(self):
        # 使用数据库连接池
        conn = Config.POOL.connection()
        self.mysql_conn = conn
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetch_all(self, sql, args):
        # 查询所有
        self.cursor.execute(sql, args)
        self.db_close()
        return self.cursor.fetchall()

    def fetch_one(self, sql, args):
        # 查询某个
        self.cursor.execute(sql, args)
        self.db_close()
        return self.cursor.fetchone()

    def insert_one(self, sql, args):
        # 插入某个
        self.cursor.execute(sql, args)
        self.mysql_conn.commit()
        self.db_close()

    def db_close(self):
        self.cursor.close()
        self.mysql_conn.close()

