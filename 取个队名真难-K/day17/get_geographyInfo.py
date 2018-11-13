#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 2:46 PM
# @Author  : liangk
# @Site    : 
# @File    : get_geographyInfo.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import datetime
from .download_img import Download_image
import json


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    request.encoding = 'gbk'
    if request.status_code == 200:
        html = request.content
    return html


def download_img(img_url, img_name):
    '''下载图片'''
    d = Download_image()
    d.makeDir('images')
    d.download(img_url, img_name, 'images')


def process_detailData(geographyInfo_list):
    """处理详情"""
    for i in geographyInfo_list:
        detail_list = i['detail']
        html = get_html(url1 + i['url'])
        soup = BeautifulSoup(html, 'lxml')
        div_list = soup.find_all(class_='big_txt')
        for i in div_list:
            detail_info = {}
            detail = i.find_all(name='a')
            title = detail[0].get_text()
            content = detail[1].get_text()
            detail_info.update({"title": title})
            detail_info.update({"content": content})
            detail_list.append(detail_info)


def process_data(img_list):
    """处理数据"""
    geographyInfo_list = []
    detail_list = []
    for image in img_list:
        img = image.find(class_='s_img')
        img_url = img['src']
        img_name = img['alt']
        # 下载图片
        download_img(img_url, img_name)

        # 写成json格式
        info_list = {}
        info_list.update({"catnames": img_name})
        info_list.update({"pic": img_url})
        info_list.update({"detail": []})
        more = image.select('p')
        for j in more:
            more_url = j.select('a')[0]['href']
            info_list.update({"url": more_url})

        articallist = []
        # 处理图片的标题
        li = image.select('li')
        for i in li:
            content = {}
            content_url = i.select('a')[0]['href']
            title = i.get_text()
            content.update({'title': title})
            content.update({'url': content_url})
            articallist.append(content)
        info_list.update({"articallist": articallist})
        geographyInfo_list.append(info_list)
    process_detailData(geographyInfo_list)
    save_by_json(geographyInfo_list)


def save_by_json(data):
    """json格式保存"""
    print('开始存储json数据……')
    with open('data.json', 'w') as file:
        json.dump(data, file)
    print('存储数据完毕！')


# 程序主入口
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    url = 'http://www.ngchina.com.cn/magazine/'
    url1 = 'http://www.ngchina.com.cn'
    html = get_html(url)

    # print('获取图片信息')
    soup = BeautifulSoup(html, 'lxml')
    # 这里选择img_list, 而不是选择img_box,不然会多出一个图片
    img_list = soup.find_all(class_='img_list')
    # img_list1 = soup.find_all('div', {"class": "img_box"})

    process_data(img_list)

    end_time = datetime.datetime.now()

    print('耗时: ', (end_time - start_time).seconds)
