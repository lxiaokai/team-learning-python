# BY LHF
import json
import os

import requests

URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=&device_id=&token=&src=web&before&limit=20'  # 要20条数据


def getRequest(n):
    requestResult = requests.get(n)
    return requestResult


if __name__ == '__main__':
    requestResult = getRequest(URL)
    print('结果=', requestResult.status_code)
    dict1 = requestResult.json()
    list = dict1['d']['list']
    # print(dict)
    # print(list)
    # text=open('text.txt','a',encoding='utf-8')  拼接的模式写入
    if os.path.exists('user') == False:
        os.makedirs('user')
    if os.path.exists('img') == False:
        os.makedirs('img')
    text = open('user/user.txt', 'w', encoding='utf-8')  # 替换的模式写入
    img = open('img/img.txt', 'w', encoding='utf-8')  # 替换的模式写入
    text.writelines('获取的到user:' + "\n")
    img.write('图片链接：' + '\n')
    for i in list:
        text.write(i['user']['username'] + '\n')  # 换行
        # text.writelines(i['user']['username'])
        img.write(str(i['pictures']) + '\n')

    text.close()
    img.close()
    with open('user/user.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    with open('img/img.txt', 'r', encoding='utf-8') as k:
        print(k.read())
