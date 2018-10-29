#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 10:26 PM
# @Author  : liangk
# @Site    : 
# @File    : task12-1.py
# @Software: PyCharm

import mysql.connector

if __name__ == "__main__":
    # change root password to yours:
    conn = mysql.connector.connect(user='root', password='liangkai', database='test')

    cursor = conn.cursor()
    # 创建user表:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入记录，注意MySQL的占位符是%s:
    # cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
    # cursor.execute('insert into user (id, name) values (%s, %s)', ('2', '肥仔'))
    # 提交事务:
    # conn.commit()
    # cursor.close()

    # 修改
    cursor.execute("update user set name = '%s' where id = '%s'" % ("李少", '11'))
    conn.commit()

    # 删除
    cursor.execute("delete from user where id='%s'"%('11'))
    conn.commit()


    # 查询所有
    cursor = conn.cursor()
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)

    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()
