#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 9:29 AM
# @Author  : liangk
# @Site    : 
# @File    : base64_test.py
# @Software: PyCharm

import base64

# 程序主入口
if __name__ == '__main__':
    # 在Python中使用BASE 64编码:
    s = base64.b64encode('肥仔'.encode('utf-8'))
    print(s)
    d = base64.b64decode(s).decode('utf-8')
    print(d)

    # 在Python中使用BASE 64编码:
    s = base64.urlsafe_b64encode('肥仔'.encode('utf-8'))
    print(s)
    d = base64.urlsafe_b64decode(s).decode('utf-8')
    print(d)
