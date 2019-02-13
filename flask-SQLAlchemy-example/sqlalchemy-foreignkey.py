#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/12 13:53
@Author  : TX
@File    : sqlalchemy-foreignkey.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import UserInfo, Department

engine = create_engine(
    "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()
# 1. 查询所有用户
# result = session.query(UserInfo).all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 2. 查询所有用户+所属部门名称
# result = session.query(UserInfo.id, UserInfo.name, Department.depart_name).join(
#     Department, UserInfo.depart_id == Department.id).all()
# for item in result:
#     print(item.id, item.name, item.depart_name)

# 3. relation字段:查询所有用户+所属部门名称
# result = session.query(UserInfo).all()
# for item in result:
#     print(item.id, item.name, item.db.depart_name)

# 4. relation字段:查询销售部所有的人员
# result = session.query(Department).filter(Department.depart_name == 'python').all()
# for item in result:
#     print(item.id, item.depart_name, [(user.id, user.name, user.depart_id) for user in item.depart])

# 5. 创建一个名称叫：IT部门，再在该部门中添加一个员工：田硕
# 方式一：
# depart = Department(depart_name='销售部')
# session.add(depart)
# session.commit()
# user = UserInfo(name='田硕', depart_id=depart.id)
# session.add(user)
# session.commit()
# 方式二：
# user = UserInfo(name='123456', db=Department(depart_name='Android'))
# session.add(user)
# session.commit()

# 6. 创建一个名称叫：王者荣耀，再在该部门中添加一个员工：龚林峰/长好梦/王爷们
depart = Department(depart_name='王者荣耀')
# 此处的depart是反向引用的名称
depart.depart = [UserInfo(name='asd'), UserInfo(name='ppp'), UserInfo(name='ewqeqe')]
session.add(depart)
session.commit()

session.close()
