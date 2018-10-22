# @time 2018/10/22 10:11
# @Author lhf

import os
from urllib import parse

import requests

URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=&device_id=&token=&src=web&before&limit=20'  # 要20条数据


def getRequest(n):
    requestResult = requests.get(n)
    return requestResult


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


def download_img(url, name):
    # 图片名称
    url_data = parse.urlparse(url=url)
    # 图片请求参数
    url_param = parse.parse_qs(url_data.query)
    try:
        # 图片扩展名
        img_ext = url_param['f'][0]  # 有可能为空
    except:
        print("error:", url_param);
        img_ext = '.jpg'
    # 图片路径
    url_path = url_data.path
    # 图片标识ID
    img_id = os.path.split(url_path)[1]
    # 图片名称
    if (name == ''):
        img_name = img_id + '.' + img_ext
    else:
        img_name = name
    img_path = os.path.join("img", img_name)
    with open(img_path, 'wb') as o:
        pic = requests.get(url)
        o.write(pic.content)


if __name__ == '__main__':
    requestResult = getRequest(URL)
    print('结果=', requestResult.status_code)
    dict1 = requestResult.json()
    list = dict1['d']['list']
    # print(dict)
    # text=open('text.txt','a',encoding='utf-8')  拼接的模式写入
    makeDir('user')
    makeDir('img')
    text = open('user/user.txt', 'w', encoding='utf-8')  # 替换的模式写入
    imgText = open('img/img.txt', 'w', encoding='utf-8')  # 替换的模式写入
    text.writelines('获取的到user:' + "\n")
    # imgText.write('图片链接：' + '\n')
    for i in list:
        text.write(i['user']['username'] + '\n')  # 换行
        for j in i['pictures']:
            imgText.writelines(j + "\n")
            download_img(j, '')
    text.close()
    imgText.close()
    with open('user/user.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    with open('img/img.txt', 'r', encoding='utf-8') as k:
        print(k.read())
