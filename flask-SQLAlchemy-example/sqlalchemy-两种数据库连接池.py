#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/14 10:01
@Author  : TX
@File    : sqlalchemy-两种数据库连接池.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models import Student

engine = create_engine(
    "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
# 第一种连接池
# SessionFactory = sessionmaker(bind=engine)
#
#
# def task():
#     # 去连接池中获取一个连接
#     session = SessionFactory()
#     ret = session.query(Student).all()
#     for item in ret:
#         print(item.id, item.name)
#     # 将连接交还给连接池
#     session.close()
#
#
# from threading import Thread
#
# for i in range(20):
#     t = Thread(target=task)
#     t.start()


# 第二种连接池-推荐
SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)


def task():
    ret = session.query(Student).all()
    for item in ret:
        print(item.id, item.name)
    # 将连接交还给连接池
    session.remove()


from threading import Thread

for i in range(20):
    t = Thread(target=task)
    t.start()









