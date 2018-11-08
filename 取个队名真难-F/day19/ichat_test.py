# @time 2018/11/5 13:50
# @Author lhf

# -*- coding=utf-8 -*-
import requests
import itchat
from bs4 import BeautifulSoup

KEY = '82622364a28142878dd8ad634eec401c'  # 肥仔的
headers_dream = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Content-Length': '13',
    'Content-Type': 'application/x-www-form-urlencoded'
}
dream_url = 'https://www.zgjm.net/search/'
# dream_body = {'keyboard': ''}
dream_dic = {}

def_text = '回复数字1，进入解梦模式\n回复数字2，进入机器人模式'
def_dream_text = "回复 解梦+内容\n如回复 '解梦+梦见蛇' ，即可解梦\n退出模式回复字母 'q' "
all_user_data = {}
user_data = {'model': 0, 'dreamModel': 0, 'dreamBody': ''}


def robot_text(msg, uid):
    # 普通机器人
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': uid,
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


def search_dream_one(uid):
    success = False
    try:
        dream_body = {'keyboard': all_user_data[uid]['dreamBody']}
        re = requests.post(url=dream_url, headers=headers_dream, data=dream_body)
        soup = BeautifulSoup(re.content, 'html.parser')
        li = soup.find('ul', class_='lib_text').find_all('li')
        dream_dic[uid] = li
        s = '输入相应数字代号查询相应结果\n输入数字0返回\n'
        for i in li:
            a = i.find('a')  # 搜索不到的时候没有a标签，直接抛异常吧
            s += str(li.index(i) + 1) + '.' + a.text + "\n"
        success = True
        return s, success
    except:
        return '对不起，没有相关解梦。请简要输入您梦到的事物即可。', success


def search_dream_two(uid, index):
    try:
        li = dream_dic[uid][int(index) - 1]
        dream_body = {'keyboard': all_user_data[uid]['dreamBody']}
        re_a = requests.post(url=dream_url.replace('/search/', li.find('a')['href']), headers=headers_dream,
                             data=dream_body)
        print(re_a.status_code)
        soup_a = BeautifulSoup(re_a.content, 'html.parser')
        article = soup_a.find('article', class_='article-content')
        p_a = article.find_all('p')
        s = ''
        for p in p_a:
            s += p.text
        s = s.replace('www.zgjm.net', 'lhf')
        return s
    except:
        return "请输入相应的数字"


def dream_text(uid, msg):
    if all_user_data[uid]['dreamModel'] == 0:
        if msg.startswith('解梦+'):
            # 爬周公数据
            all_user_data[uid]['dreamBody'] = msg.split('+')[1]
            s, success = search_dream_one(uid)
            if success:
                all_user_data[uid]['dreamModel'] = 1  # 修改成第二阶段
            return s
        else:
            return def_dream_text
    elif all_user_data[uid]['dreamModel'] == 1:  # 第二阶段
        if msg == '0':
            all_user_data[uid]['dreamModel'] = 0  # 修改成第一阶段
            return def_dream_text
        s = search_dream_two(uid, msg)
        return s


def get_response(msg, uid):
    try:
        model = all_user_data[uid]['model']
        if msg == 'q':
            all_user_data[uid]['model'] = 0
            all_user_data[uid]['dreamModel'] = 0  # 修改成第一阶段
            return def_text
        if model == 0:  # 无模式
            if msg == '1':
                all_user_data[uid]['model'] = 1
                return '进入解梦模式\n' + def_dream_text
            elif msg == '2':
                all_user_data[uid]['model'] = 2
                return "嗨，我是vv小冰，很高兴遇见你~\n回复字母'q'退出模式"
            else:
                return def_text
        elif model == 1:  # 解梦模式

            return dream_text(uid, msg)
        elif model == 2:  # 机器人模式
            return robot_text(msg, uid)
    except Exception as e:
        all_user_data[uid]['model'] = 0
        all_user_data[uid]['dreamModel'] = 0
        return def_text


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    if not all_user_data.keys().__contains__(msg['FromUserName']):  # 没有包含该用户,初始化model 为0
        all_user_data[msg['FromUserName']] = {'model': 0, 'dreamModel': 0, 'dreamBody': ''}

    print(msg)
    print("输入：", msg['Text'])
    reply = get_response(msg['Text'], msg['FromUserName'])
    print("回复：", reply)
    return reply


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
