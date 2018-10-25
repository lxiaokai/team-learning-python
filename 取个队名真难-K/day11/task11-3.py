#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 5:47 PM
# @Author  : liangk
# @Site    : 
# @File    : task11-3.py
# @Software: PyCharm

import requests

# 程序主入口
if __name__ == '__main__':
    url = 'http://img.shujuren.org/pictures/GB/57ff13a89b3b8.png'
    r = requests.get(url)
    with open('img.png', 'wb') as f:
        f.write(r.content)
        print('写入完毕!')

    url1 = 'http://www.runoob.com/try/demo_source/movie.mp4'
    r1 = requests.get(url1)
    with open('movie.mp4', 'wb') as f:
        f.write(r1.content)
        print('写入完毕!')

    url2 = 'http://www.ytmp3.cn/down/54131.mp3'
    r2 = requests.get(url2)
    with open('Palstinalied.mp3', 'wb') as f:
        f.write(r2.content)
        print('写入完毕!')
