#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 2:11 PM
# @Author  : liangk
# @Site    : 
# @File    : juejin_followers.py
# @Software: PyCharm

import requests
import json


def get_follower_data(url, data):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    params = {}
    params.update({'uid': '59b0de6e5188250f4850ea06'})
    params.update({'currentUid': '59b0de6e5188250f4850ea06'})
    params.update({'src': 'web'})
    params.update({'before': data})
    request = requests.get(url=url, params=params, headers=header)
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
    request_url = 'https://follow-api-ms.juejin.im/v1/getUserFollowerList'
    create_date = ''
    follower_list = []
    while True:
        datalist = get_follower_data(request_url, create_date)
        if not datalist:
            break
        for i in datalist:
            print('关注>>>', 'ID:', i['follower']['objectId'], '昵称:', i['follower']['username'])
            create_date = i['createdAtString']
            follower_list.append(i['follower'])

    print('一共关注了%s人' % len(follower_list))
    save_by_json(datalist)
