#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 3:13 PM
# @Author  : liangk
# @Site    :
# @File    : get_douban_books.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import datetime
import requests

article_tag_list = []
article_type_list = []


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    request.encoding = 'gbk'
    if request.status_code == 200:
        html = request.content
    return html


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
            # for i in article_type_list[0]:
            # for start in range(0, 1):
            # (start * 20) 分页是0 20  40 这样的
            # type=S是按评价排序
            url = base_url + sub1 + '?start=%s' % 0 + '&type=S'
            title = '==============' + sub1 + '=============='
            print(title)
            print(url)
            with open('book.text', 'a') as f:
                f.write('\n' + title + '\n')
                f.write(url + '\n')
            html = get_html(url)
            soup = BeautifulSoup(html, 'lxml')
            li = soup.find_all(class_='subject-item')
            for div in li:
                info = div.find(class_='info').find('a')
                img = div.find(class_='pic').find('img')
                content = '书名:<%s>' % info['title'] + '  书名图片:' + img['src'] + '\n'
                print(content)
                with open('book.text', 'a') as f:
                    f.write(content)

    end_time = datetime.datetime.now()
    print('耗时: ', (end_time - start_time).seconds)
