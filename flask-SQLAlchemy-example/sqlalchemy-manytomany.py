#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/13 18:33
@Author  : TX
@File    : sqlalchemy-manytomany.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Course, Student2Course

engine = create_engine(
    "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

# 1. 本方法录入数据，没有加relationship
# session.add_all([
#     Student(name='大哥'),
#     Student(name='小弟'),
#     Course(title='python'),
#     Course(title='java')
# ])
# session.commit()
# session.add(Student2Course(student_id=1, course_id=1))
# session.commit()

# 2. 三张表关联
# result = session.query(Student2Course.id, Student.name, Course.title).\
#     join(Student, Student2Course.student_id == Student.id, isouter=True).\
#     join(Course, Student2Course.course_id == Course.id, isouter=True).all()
# for item in result:
#     print(item.id, item.name, item.title)

# 3. 查询大哥选的所有课
# result = session.query(Student2Course.id, Student.name, Course.title).\
#     join(Student, Student2Course.student_id == Student.id, isouter=True).\
#     join(Course, Student2Course.course_id == Course.id, isouter=True).filter(Student.name == '大哥').all()
# for item in result:
#     print(item.id, item.name, item.title)

# 使用relationship,查询大哥所选的课
# result = session.query(Student).filter(Student.name == '大哥').first()
# print(result.name, [(course.id, course.title) for course in result.course_list])

# 4. 选了“python”的所有人
# result = session.query(Student2Course.id, Course.title, Student.name).\
#     join(Course, Course.id == Student2Course.course_id, isouter=True).\
#     join(Student, Student2Course.student_id == Student.id, isouter=True).filter(Course.title == 'python').all()
# print(result)
# for item in result:
#     print(item.id, item.name, item.title)

# 使用relationship，查询选了python课程的学生
# result = session.query(Course).filter(Course.title == 'python').first()
# print(result.title, [(student.id, student.name) for student in result.student_list])

# 5. 使用relationship创建一个课程，创建2学生，两个学生选新创建的课程。
course = Course(title='ios')
course.student_list = [Student(name='张珊'), Student(name='历史')]
session.add(course)
session.commit()

session.close()

