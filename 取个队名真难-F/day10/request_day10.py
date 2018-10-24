# @time 2018/10/24 15:01
# @Author lhf

import os
import time

import requests

# URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=&device_id=&token=&src=web&before&limit=100'  # 要100条数据
URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend'
uid = ''
device_id = ''
token = ''
src = 'web'
before = ''
limit = '100'


# 抓取五百条user：uid  数据

def get_request_list():
    # request_result = requests.get(URL, uid+'&'+device_id+'&'+token+'&'+src+'&'+before+'&'+limit)
    params = {'uid': uid, 'device_id': device_id, 'token': token, 'src': src, 'before': before, 'limit': limit}
    request_result = requests.get(URL, params)
    d = request_result.json()
    print(d)
    if not d['s'] == 1:
        print(d['m'])
        # quit()  # 退出程序
        return ''

    lis = d['d']['list']
    return lis


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


if __name__ == '__main__':
    makeDir('user')
    with open('user/user.txt', 'w', encoding='utf-8') as f:
        f.write('开始时间：'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')

    text = open('user/user.txt', 'a', encoding='utf-8')  # 拼接的模式写入
    # list[0]['createdAt']
    num = 5  # 请求五次
    line = 0
    while num > 0:
        lis = get_request_list()
        if not len(lis):
            print('数据出错')
            quit()
            break
        before = lis[-1]['createdAt']  # 分页的参数
        for i in lis:
            line += 1
            s = '沸点' + str(line) + ':username=' + i['user']['username'] + ',uid=' + i['uid'] + '\n'
            text.write(s)  # 换行
        num -= 1

    text.close()
    with open('user/user.txt', 'a', encoding='utf-8') as f:
        f.write('完成时间：'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    with open('user/user.txt', 'r', encoding='utf-8') as f:
        print(f.read())
