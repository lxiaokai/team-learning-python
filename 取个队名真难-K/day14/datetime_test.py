#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 9:18 AM
# @Author  : liangk
# @Site    : 
# @File    : datetime_test.py
# @Software: PyCharm

from datetime import datetime

# 程序主入口
if __name__ == '__main__':

    # 获取当前datetime
    now = datetime.now()
    print(now)

    # 用指定日期时间创建datetime
    dt = datetime(2018, 10, 31, 9, 0)
    print(dt)
    print(dt.timestamp())

    # timestamp转换为datetime
    t = 1540947600.0
    print(datetime.fromtimestamp(t))

    # 本地时间
    print(datetime.fromtimestamp(dt.timestamp()))

    # UTC时间
    print(datetime.utcfromtimestamp(dt.timestamp()))

    # str转换为datetime
    c_day = datetime.strptime('2018-8-8 18:18:8', '%Y-%m-%d %H:%M:%S')
    print(c_day)

    # datetime转换为str
    now = datetime.now()
    print(now.strftime('%a, %b %d %H:%M'))
