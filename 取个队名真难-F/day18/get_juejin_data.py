# @time 2018/11/6 13:44
# @Author lhf
from datetime import datetime

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
URL = 'https://follow-api-ms.juejin.im/v1/getUserFollowerList'
params = {'before': '', 'uid': '', 'currentUid': '', 'src': 'web'}
uid_list_h = ['59b0de6e5188250f4850ea06']  # 把爬过的用户id存起来
name_list_h = ['gxcuizy']


def get_follower_json(uid, name):
    print("爬取'%s'的关注者" % (name))
    follow_json = {'followerNum': 0, 'followerList': []}
    num = 0
    params['uid'] = uid
    params['before'] = ''
    uid_list = []
    name_list = []
    while True:
        re = requests.get(URL, params=params, headers=headers).json()
        if not re:
            break
        dr = dict(re)
        if not dr.get('d', False):  # 获取不到d 或者没有d数据则退出循环
            break
        followerList = dr['d']
        params['before'] = followerList[-1]['createdAtString']  # 下一页参数
        num += len(followerList)
        for fl in followerList:
            f = {'userId': fl['follower']['objectId'], 'userName': fl['follower']['username']}
            follow_json['followerList'].append(f)
            uid_list.append(fl['follower']['objectId'])
            name_list.append(fl['follower']['username'])

    follow_json['followerNum'] = num  # 关注数量
    print(follow_json)
    return uid_list, name_list


def get_all(uid_list, name_list):
    for u in uid_list:
        if not uid_list_h.__contains__(u):  # 没有爬过的爬一下
            uid_list_h.append(u)  # 添加uid
            name_list_h.append(name_list[uid_list.index(u)])  # 添加name
            uid_list1, name_list1 = get_follower_json(u, name_list[uid_list.index(u)])
            # 回调
            get_all(uid_list1, name_list1)


if __name__ == '__main__':
    # 获取当前时间戳
    start_time = datetime.now().timestamp()
    print('开始时间：', datetime.now())

    uid_list, name_list = get_follower_json('59b0de6e5188250f4850ea06', 'gxcuizy')
    get_all(uid_list, name_list)

    print(uid_list_h)
    print(name_list_h)

    print("爬了%s次" % (len(uid_list_h)))
    print("结束时间：", datetime.now())
    end_time = datetime.now().timestamp()
    print('总用时：', end_time - start_time)
