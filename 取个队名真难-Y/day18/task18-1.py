#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

def get_follower_data(url, data):
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    # 对于带参数的URL，传入一个dict作为params参数
    params = {}
    params.update({'uid': '579969d7128fe100541207e0'})
    params.update({'currentUid': '579969d7128fe100541207e0'})
    params.update({'src': 'web'})
    params.update({'before': data})
    request = requests.get(url = url,params = params, headers = header)
    if request.status_code == 200:
        return request.json()['d']

def sava_data(data):
    with open('follower.json','w') as file:
        json.dump(data,file)
    print('存储完毕')

if __name__ == '__main__':
    url = 'https://follow-api-ms.juejin.im/v1/getUserFollowerList'
    data = ''
    followers = []
    print('关注柚子茶的小可爱：')
    while True:
        follower = {}
        data_list = get_follower_data(url,data)
        if not data_list:
            break
        for i in data_list:
            data = i['createdAtString']
            follower.update({'ID': i['follower']['objectId']})
            follower.update({'username': i['follower']['username']})
            # print('ID',i['follower']['objectId'], '昵称：',i['follower']['username'])
            followers.append(follower)
            print(follower)
    sava_data(followers)