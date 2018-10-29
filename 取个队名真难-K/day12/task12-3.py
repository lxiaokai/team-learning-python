#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 9:17 AM
# @Author  : liangk
# @Site    : 
# @File    : task12-3.py
# @Software: PyCharm

import pymysql


def show_version():
    # 创建一个连接
    conn = pymysql.connect(user='root', password='liangkai', database='test')
    # 用cursor()创建一个游标对象
    cursor = conn.cursor()
    # 使用execute()执行一个mysql语句查询
    cursor.execute('select version();')
    # 使用fetchone()获取一条数据
    mysql_version = cursor.fetchone()
    print(mysql_version)
    # 关闭连接
    cursor.close()
    conn.close()


def create_table():

    # 创建一个连接
    db = pymysql.connect(user='root', password='liangkai', database='test')
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 如果表存在则删除
    print('开始建表')
    cursor.execute("DROP TABLE IF EXISTS %s" % 'user')
    # 表结构sql
    sql = 'create table user (id varchar(20) primary key, name varchar(20))'
    # 执行建表
    cursor.execute(sql)
    # 关闭连接
    cursor.close()
    db.close()
    print('建表成功！')


# 程序主入口
if __name__ == '__main__':
    show_version()

    create_table()

    # 这个和基本的一样的使用方法....
