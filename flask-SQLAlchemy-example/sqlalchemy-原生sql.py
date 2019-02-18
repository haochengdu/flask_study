#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/14 13:49
@Author  : TX
@File    : sqlalchemy-原生sql.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine(
    "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
SessionFactory = sessionmaker(bind=engine)
# session = scoped_session(SessionFactory)
session = SessionFactory()
# 查询python课程的人员
# 方式一
# sql = "SELECT student.name FROM student2course " \
#       "LEFT JOIN course ON (student2course.course_id = course.id) " \
#       "LEFT JOIN student ON (student2course.student_id = student.id) " \
#       "WHERE course.title=:course_title"
# cursor = session.execute(sql, params={'course_title': 'python'})
# result = cursor.fetchall()
# print(result)
# 将连接交还给连接池
# session.remove()
# session.close()


# 方式二：
conn = engine.raw_connection()
cursor = conn.cursor()
sql = "SELECT student.name FROM student2course " \
      "LEFT JOIN course ON (student2course.course_id = course.id) " \
      "LEFT JOIN student ON (student2course.student_id = student.id) " \
      "WHERE course.title=%s"
cursor.execute(sql, args=('python',))
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()







