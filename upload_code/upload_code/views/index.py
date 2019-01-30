#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 11:22
@Author  : TX
@File    : index.py
@Software: PyCharm
主页功能
"""
import os
import shutil
import uuid

import datetime
from flask import Blueprint, render_template, request, session, redirect, url_for
from utils.mysqldb import MySQLHelper


up_index = Blueprint('up_index', __name__)


@up_index.route('/home')
def home():

    return render_template('home.html')


@up_index.route('/user_list')
def user_list():
    # 显示所有用户
    # 从数据库中查询所有用户
    try:
        mysql_helper = MySQLHelper()
        sql = 'SELECT id,userName,nickName FROM userInfo'
        users = mysql_helper.fetch_all(sql, ())
    except Exception as e:
        return 'MySQL错误= {}'.format(e)
    return render_template('user_list.html', data_list=users)


@up_index.route('/detail/<int:uid>')
def detail(uid):
    # 查看某个用户代码上传详情
    if isinstance(uid, int):  # flask已经帮我们做了，当uid不为int时404
        # 根据当前用户ID查询
        try:
            mysql_helper = MySQLHelper()
            sql = 'SELECT u.userName,c.codeLines, c.createTime ' \
                  'FROM codeRecord c ' \
                  'LEFT OUTER JOIN userInfo u ' \
                  'ON u.id=c.userId ' \
                  'where u.id=%s'
            upload_code_infos = mysql_helper.fetch_all(sql, (uid, ))
        except Exception as e:
            return 'MySQL错误= {}'.format(e)
        return render_template('detail.html', record_list=upload_code_infos)
    return '参数必须为用户的ID（int类型）'


@up_index.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    # post逻辑
    # 判断文件是.zip还是.py结尾。zip解压后保存到指定的目录
    # 解压后遍历每一文件夹统计其行数
    today_start_time = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
    today_end_time = today_start_time.split(' ')[0] + ' 23:59:59'
    # 从session中获取用户ID
    uid = session['user_info']['id']
    file_obj = request.files.get('code', None)  # 一定要先取文件，不然会造成重复访问该接口
    # 先判断当天是否已经上传过，当天上传过不能上传
    try:
        mysql_helper = MySQLHelper()
        sql = 'SELECT * FROM codeRecord WHERE userId=%s AND createTime BETWEEN %s AND %s'
        recodes = mysql_helper.fetch_all(sql, (uid, today_start_time, today_end_time))
        if recodes:
            return '今天已经上传过了'
    except Exception as e:
        return 'MySQL错误= {}'.format(e)
    if file_obj:
        file_name = file_obj.filename
        file_stream = file_obj.stream
        # 代码行数统计
        count = 0
        cwd = os.getcwd()
        save_dir = os.path.join(cwd, 'files', str(uuid.uuid4()).replace('-', ''))
        os.makedirs(save_dir)  # 创建文件夹
        
        if file_name.endswith('.py'):
            save_path = os.path.join(save_dir, file_name)
            file_obj.save(save_path)
            with open(save_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:  # 换行
                        continue
                    if line.startswith(b'#'):
                        continue
                    count += 1
        elif file_name.endswith('.zip'):
            # shutil._unpack_zipfile(file_stream, save_dir)  # 调用保护方法
            # 先保存后解压
            # save_path = os.path.join(save_dir, file_name)
            # file_obj.save(save_path)
            # shutil.unpack_archive(save_path, save_dir, format='zip')  # format参数必须加
            # zip支持直接解压，tar包需要先保存后解压
            shutil.unpack_archive(file_stream, save_dir, format='zip')  # format参数必须加

            for base_path, dirs, files in os.walk(save_dir):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(base_path, file)
                        with open(file_path, 'rb') as f:
                            for line in f:
                                line = line.strip()
                                if not line:  # 换行
                                    continue
                                if line.startswith(b'#'):
                                    continue
                                count += 1
        else:
            return '请上传.py和.zip类型的文件'
        # 存入数据库
        try:
            # 时间
            c_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 从session中获取用户ID
            # uid = session['user_info']['id']
            mysql_helper = MySQLHelper()
            sql = 'INSERT INTO codeRecord (codeLines,createTime,userId) VALUES (%s,%s,%s)'
            mysql_helper.insert_one(sql, (count, c_time, uid))
        except Exception as e:
            return 'MySQL错误= {}'.format(e)
        url = url_for('up_index.detail', uid=uid)
        # return redirect('/detail/{}'.format(uid))
        return redirect(url)






