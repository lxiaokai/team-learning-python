#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 4:37 PM
# @Author  : liangk
# @Site    : 
# @File    : GuessYouLike.py
# @Software: PyCharm

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import time
import requests
from urllib import parse

image_urlList = []
book_nameList = []


def download_img(url):
    """下载图片文件"""
    request = requests.get(image_urlList[i])
    if request.status_code == 200:
        base_name = os.path.basename(image_urlList[i])
        print('正在下载图片-%s' % book_nameList[i])
        with open('%s.jpg' % book_nameList[i], 'wb') as img:
            img.write(request.content)
            print('图片下载完成！')
    else:
        print('图片下载路径错误！')


def download_content(i):
    with open('%s.txt' % book_nameList[i], 'w') as file:
        file.write('图片: %s\n' % image_urlList[i])
        file.write('内容: %s\n' % book_nameList[i])
        file.write('\n\n\n')
        print('文件创建成功 %s' % os.path.join(path, '%s.txt' % book_nameList[i]))


def getData(url):
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    div = soup.find('div', {"class": "widget d_postlist"})

    # 图
    image_links = div.find_all('img', {'src': re.compile('https://cuiqingcai.*')})
    for url in image_links:
        image_urlList.append(url['src'])

    # 书名字
    span = div.find_all('span', {'class': 'text'})
    for content in span:
        book_nameList.append(content.get_text())


# 程序主入口
if __name__ == '__main__':

    url = 'https://cuiqingcai.com/5548.html'
    getData(url)

    path = '猜你喜欢'
    # 判断,是否创建
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)

    for i in range(0, len(image_urlList)):
        download_img(i)
        download_content(i)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
