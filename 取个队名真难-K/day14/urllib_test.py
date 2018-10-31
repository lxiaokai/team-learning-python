#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 9:31 AM
# @Author  : liangk
# @Site    : 
# @File    : urllib_test.py
# @Software: PyCharm

from urllib import request, parse

# 程序主入口
if __name__ == '__main__':
    with request.urlopen('https://baike.baidu.com/item/%E9%87%91%E5%BA%B8/128951?fr=aladdin') as f:
        data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
