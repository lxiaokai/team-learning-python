#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22
# @Author  : liangk
# @Site    :
# @File    : get_douban_books.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import datetime
import requests
import json
import random

ip_random = -1
article_tag_list = []
article_type_list = []


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    global ip_random
    ip_rand, proxies = get_proxie(ip_random)
    print(proxies)
    try:
        request = requests.get(url=url, headers=header, proxies=proxies, timeout=3)
    except:
        request_status = 500
    else:
        request_status = request.status_code
    print(request_status)
    while request_status != 200:
        ip_random = -1
        ip_rand, proxies = get_proxie(ip_random)
        print(proxies)
        try:
            request = requests.get(url=url, headers=header, proxies=proxies, timeout=3)
        except:
            request_status = 500
        else:
            request_status = request.status_code
        print(request_status)
    ip_random = ip_rand
    request.encoding = 'gbk'
    html = request.content
    print(html)
    return html


def get_proxie(random_number):
    with open('ip.txt', 'r') as file:
        ip_list = json.load(file)
        if random_number == -1:
            random_number = random.randint(0, len(ip_list) - 1)
        ip_info = ip_list[random_number]
        ip_url_next = '://' + ip_info['address'] + ':' + ip_info['port']
        proxies = {'http': 'http' + ip_url_next, 'https': 'https' + ip_url_next}
        return random_number, proxies


# 程序主入口
if __name__ == '__main__':



    """只是爬取了书籍的第一页,按照评价排序"""
    start_time = datetime.datetime.now()

    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    base_url = 'https://book.douban.com/tag/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    article_tag_list = soup.find_all(class_='tag-content-wrapper')
    tagCol_list = soup.find_all(class_='tagCol')

    for table in tagCol_list:
        """ 整理分析数据 """
        sub_type_list = []
        a = table.find_all('a')
        for book_type in a:
            sub_type_list.append(book_type.text)
        article_type_list.append(sub_type_list)

    for sub in article_type_list:
        for sub1 in sub:
            title = '==============' + sub1 + '=============='
            print(title)
            print(base_url + sub1 + '?start=0' + '&type=S')
            with open('book.text', 'a', encoding='utf-8') as f:
                f.write('\n' + title + '\n')
                f.write(url + '\n')
            for start in range(0, 2):
                # (start * 20) 分页是0 20  40 这样的
                # type=S是按评价排序
                url = base_url + sub1 + '?start=%s' % (start * 20) + '&type=S'
                html = get_html(url)
                soup = BeautifulSoup(html, 'lxml')
                li = soup.find_all(class_='subject-item')
                for div in li:
                    info = div.find(class_='info').find('a')
                    img = div.find(class_='pic').find('img')
                    content = '书名:<%s>' % info['title'] + '  书本图片:' + img['src'] + '\n'
                    print(content)
                    with open('book.text', 'a', encoding='utf-8') as f:
                        f.write(content)

    end_time = datetime.datetime.now()
    print('耗时: ', (end_time - start_time).seconds)
