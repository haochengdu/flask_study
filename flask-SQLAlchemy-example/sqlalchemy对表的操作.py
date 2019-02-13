#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/11 23:05
@Author  : TX
@File    : sqlalchemy对表的操作.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UserInfo

engine = create_engine(
    "mysql+pymysql://root:oldboy@192.168.2.223:3306/sqlalchemy_study?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()
# ############################## 基本增删改查 ###############################
# 1. 增加
# 1.1增加一个
# obj1 = UserInfo(name='dandan')
# session.add(obj1)
# session.commit()
# 1.2增加多个
# session.add_all(
#     [
#         UserInfo(name='haha'),
#         UserInfo(name='xixi')
#     ]
# )
# session.commit()

# 查询
# result = session.query(UserInfo).all()  # 返回一个列表，列表中是UserInfo的实例化对象
# for item in result:
#     print(item.id, item.name, item.depart_id)

# result = session.query(UserInfo).filter(UserInfo.id >= 2)
# for item in result:
#     print(item.id, item.name, item.depart_id)

# result = session.query(UserInfo).filter(UserInfo.id >= 2).first()  # 当first后返回UserInfo的实例化对象
# print(result.id, result.name, result.depart_id)

# 删除
# session.query(UserInfo).filter(UserInfo.name == 'xixi').delete()
# session.commit()

# 改
# session.query(UserInfo).filter(UserInfo.name == 'dandan').update({UserInfo.depart_id: 22})
# session.commit()

# session.query(UserInfo).filter(UserInfo.name == 'dandan').update({'depart_id': 222})
# session.query(UserInfo).filter(UserInfo.name == 'dandan').update(
#     {'name': UserInfo.name + '123'}, synchronize_session=False)  # 字符串相加
# session.commit()

# ############################## 其他常用 ###############################
# 1. 指定列查询
# result = session.query(UserInfo.id, UserInfo.name.label('username')).all()  # 返回列表，列表里包含元组，元组为查询的每行结果，同时包含了列名属性
# for item in result:
#     print(item.id, item.username)
#     print(item[0], item[1])

# 2. 默认条件and
# result = session.query(UserInfo.name).filter(UserInfo.depart_id > 100, UserInfo.id >= 1).all()
# for item in result:
#     print(item.name)

# 3. between
# result = session.query(UserInfo).filter(UserInfo.depart_id.between(1, 10)).all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 4. in
# result = session.query(UserInfo).filter(UserInfo.id.in_([1, 2, 3, 4])).all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 5. 子查询
# result = session.query(UserInfo).filter(UserInfo.id.in_([1, 2, 3, 4])).filter(UserInfo.name == 'haha').all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 6. and 和 or
# result = session.query(UserInfo).filter(UserInfo.id > 1, UserInfo.depart_id > 1).all()  # 默认是and
# from sqlalchemy import and_, or_
# # result = session.query(UserInfo).filter(and_(UserInfo.id > 1, UserInfo.depart_id > 1)).all()
# # result = session.query(UserInfo).filter(or_(UserInfo.id > 1, UserInfo.depart_id > 1)).all()
# result = session.query(UserInfo).filter(or_(
#     UserInfo.depart_id > 3,
#     and_(UserInfo.id > 1, UserInfo.name == 'haha'),
#     UserInfo.depart_id == 3
# ))
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 7. filter_by
# result = session.query(UserInfo).filter_by(name='dandan').all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 8. 通配符
# result = session.query(UserInfo).filter(UserInfo.name.like('%a')).all()
# result = session.query(UserInfo).filter(~UserInfo.name.like('%a')).all()
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 9. 切片
# result = session.query(UserInfo).filter(UserInfo.depart_id > 1).all()[0:]
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 10.排序
# result = session.query(UserInfo).order_by(UserInfo.depart_id.desc(), UserInfo.id.asc())
# for item in result:
#     print(item.id, item.name, item.depart_id)

# 11. group by
# from sqlalchemy import func
# # result = session.query(UserInfo.depart_id, func.count(UserInfo.id).label('num')).group_by(UserInfo.depart_id)
# result = session.query(UserInfo.depart_id, func.count(UserInfo.id).label('num'))\
#     .group_by(UserInfo.depart_id).having(func.count(UserInfo.id) > 1)
# for item in result:
#     print(item.depart_id, item.num)

# 12.union 和 union all 两种查询合在一起。查询的字段必须一样
"""
select id,name from users
UNION
select id,name from users;
"""
q1 = session.query(UserInfo)
q2 = session.query(UserInfo).filter(UserInfo.id > 2)
# result = q1.union(q2).all()
result = q1.union_all(q2).all()
for item in result:
    print(item.id, item.name, item.depart_id)

session.close()

