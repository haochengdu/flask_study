#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/11 15:36
@Author  : TX
@File    : sqlalchemy对表的操作.py
@Software: PyCharm
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Department(Base):
    """
    部门表
    """
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    depart_name = Column(String(32), nullable=False)


class UserInfo(Base):
    """
    创建表
    """
    __tablename__ = 'userinfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    depart_id = Column(Integer, ForeignKey('department.id'), default=1)
    db = relationship('Department', backref='depart')  # 反向关联的名字


def create_tables():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.create_all(engine)


def drop_tables():
    """
    根据类删除所有的表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.drop_all(engine)


if __name__ == '__main__':

    create_tables()
    # drop_tables()


