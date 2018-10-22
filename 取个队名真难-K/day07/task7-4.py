#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 3:13 PM
# @Author  : liangk
# @Site    : 
# @File    : task7-4.py
# @Software: PyCharm

import requests
import os
from urllib.request import urlretrieve

# 程序主入口
if __name__ == '__main__':

    # r = requests.get('https://github.com/lxiaokai/team-learning-python')
    # print(r.status_code)
    # print(r.text)
    # print(r.content)
    # print(r.json())

    print('开始获取沸点数据~ 请稍后')
    r = requests.get('https://short-msg-ms.juejin.im/v1/pinList/recommend?'
                     'uid=5bbf1f7fe51d450e8108eec4&device_id=1539252094995'
                     '&token=eyJhY2Nlc3NfdG9rZW4iOiJRVUs1RWZObDByTDd6UWkwIi'
                     'wicmVmcmVzaF90b2tlbiI6ImpEc1NpaDlYUEZscHVuQloiLCJ0b2t'
                     'lbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D'
                     '&src=web&before&limit=30')
    if r.status_code == 200:
        print('请求成功')
        dataList = r.json()['d']['list']
        # print(len(dataList), dataList)
        userList = []
        # print(dataList[0])
        '''
            保存沸点图片、沸点内容、发布沸点的用户信息等，保存的格式不限,注意: 一个沸点一个文件夹
        '''

        for i in range(0, len(dataList)):
            # 用户昵称
            username = dataList[i]['user']['username']
            # 用户头像
            avatarLarge = dataList[i]['user']['avatarLarge']
            # 内容
            content = dataList[i]['content']
            # 内容图片
            pictures = dataList[i]['pictures']
            # 创建一个文件夹来装图片
            # 判断是否创建文件夹
            dirPath = os.getcwd() + '/' + username
            print(dirPath)
            if os.path.exists(os.getcwd() + '/' + username):

                # 开始写文件
                print('开始下载头像~')
                r = requests.get(avatarLarge)
                with open(dirPath + '/avatarLarge.jpg', 'wb') as f:
                    f.write(r.content)
                    print('头像下载完毕!')

                print('开始写用户信息文本~')
                with open(dirPath + '/user.txt', 'w') as f:
                    f.write('名字: ' + username)
                    f.write('\n头像链接: ' + avatarLarge)
                    print('用户信息文本写完毕!')

                print('开始写内容文本~')
                with open(dirPath + '/content.txt', 'w') as f:
                    f.write('内容: ' + content)
                    print('内容文本写完毕!')

                if len(pictures) > 0:
                    picturesPath = dirPath + '/pictures'
                    if os.path.exists(picturesPath):
                        for i in range(0, len(pictures)):
                            r = requests.get(pictures[i])
                            print('开始下载内容图片~')
                            with open(picturesPath + '/%s.jpg' % i, 'wb') as f:
                                f.write(r.content)
                                print('内容图片下载完毕!')
                    else:
                        os.mkdir(picturesPath)
            else:
                os.mkdir(dirPath)
    else:
        print('请求失败')
