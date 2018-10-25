#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 5:41 PM
# @Author  : liangk
# @Site    : 
# @File    : task10-1.py
# @Software: PyCharm

import os
import requests
import time


# 请求数据
def request_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['d']['list']


# 追加数据
def additional_copy():
    os.chdir('..')
    for root, dirs, files in os.walk(path):
        for name in files:
            with open(os.path.join(os.getcwd() + '/' + root, name), 'a') as f:
                f.write('\t\t\t\t-----------------------------\n')
                f.write('\t\t\t\t-----------------------------\n')
                f.write('\t\t\t\t-------------肥仔-------------\n')
                f.write('\t\t\t\t-------------肥仔-------------\n')
                f.write('\t\t\t\t-------------肥仔-------------\n')
                f.write('\t\t\t\t-----------------------------\n')
                f.write('\t\t\t\t-----------------------------\n')
    print('-------------    追加数据完毕    -------------')


# 程序主入口
if __name__ == '__main__':

    url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=5bbf1f7fe51d450e8108eec4&device_id=1539252094995&token=eyJhY2Nlc3NfdG9rZW4iOiJRVUs1RWZObDByTDd6UWkwIiwicmVmcmVzaF90b2tlbiI6ImpEc1NpaDlYUEZscHVuQloiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D&src=web&before&limit=30'

    path = 'juejin'
    # 判断,是否创建
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    dataList = request_data(url)
    for i in dataList:
        user = i['user']
        with open('%s.txt' % user['username'], 'w') as file:
            file.write('头像链接: %s\n' % user['avatarLarge'])
            file.write('内容: %s\n' % i['content'])
            file.write('\n\n\n')
            print('文件创建成功 %s' % os.path.join(path, '%s.txt' % i['user']['username']))

    print('-------------追加数据到每个文件后面-------------')
    print('请稍后~')
    # 假装很慢
    time.sleep(2)
    additional_copy()
