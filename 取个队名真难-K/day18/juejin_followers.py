#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 2:11 PM
# @Author  : liangk
# @Site    : 
# @File    : juejin_followers.py
# @Software: PyCharm

import requests
import json


def get_follower_data(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    if request.status_code == 200:
        return request.json()['d']


def save_by_json(data):
    """json格式保存"""
    print('开始存储json数据……')
    with open('follower_list.json', 'w') as file:
        json.dump(data, file)
    print('存储数据完毕！')


# 程序主入口
if __name__ == '__main__':
    request_url = 'https://follow-api-ms.juejin.im/v1/getUserFollowerList?uid=5bbf1f7fe51d450e8108eec4&currentUid=5bbf1f7fe51d450e8108eec4&src=web'
    datalist = get_follower_data(request_url)
    follower_list = []
    for i in datalist:
        print('关注>>>', 'ID:', i['follower']['objectId'], '昵称:', i['follower']['username'])
    print('一共关注了%s人' % len(datalist))
    save_by_json(datalist)
