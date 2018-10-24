#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
def get_data(url):
    request = requests.get(url)
    result = request.json()
    return result

if __name__ =="__main__":
    data_url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=57996b8b1532bc00605e76b6&device_id=1540377340137&token=eyJhY2Nlc3NfdG9rZW4iOiJHQVFaMVVsSVNwU1ZrWGdZIiwicmVmcmVzaF90b2tlbiI6IjBjaXVWVVJDbk1HemN1WHgiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D&src=web&before&limit=30'
    data_result = get_data(data_url)
    data_list = data_result['d']['list']
    with open('data.txt','w',encoding = 'utf-8') as file:
        for data in data_list:
            user_name = data['user']['username']
            content = data['content']
            file.write('沸点用户:'+user_name+'\n')
            file.write(content + '\n\n')
            file.write('***--------------***'+'\n')

    print(data_list)
