#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 4:44 PM
# @Author  : liangk
# @Site    : 
# @File    : getStreetAgency.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import os
import requests


def getData(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    if request.status_code == 200:
        html = request.content
        return html
    else:
        print('请求链接错误!')
        return -1



# 程序主入口
if __name__ == '__main__':

    path = '街道办事处信息'
    # 判断,是否创建
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)

    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    baseUrl1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    baseUrl1_1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/12/'
    baseUrl2 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/11/01/'

    html = getData(url)
    print(html)
    soup = BeautifulSoup(html, features='lxml')
    tr = soup.find_all('tr', {"class": "provincetr"})

    for i in tr:
        a = i.find_all('a')
        for j in a:
            print('====================================')
            print(j.get_text())
            html1 = getData(baseUrl+j['href'])
            soup1 = BeautifulSoup(html1, features='lxml')
            tr1 = soup1.find_all('tr', {"class": "citytr"})
            for i in tr1:
                a1 = i.find_all('a')
                print('====================================')
                print(a1[-1].string + '   ' +  a1[0].string + '   ' +  a1[-1]['href'])

                # 区
                html2 = getData(baseUrl+a1[-1]['href'])
                soup2 = BeautifulSoup(html2, features='lxml')
                tr2 = soup2.find_all('tr', {"class": "countytr"})
                for j in tr2:
                    muted = j.find_all('a')
                    if len(muted) > 0:
                        print(muted)
                        print(baseUrl1+muted[0]['href'])
                        if len(muted[0]['href']) > 0:

                            url = baseUrl1 + muted[0].string[0:2] + '/' + muted[0]['href']
                            html3 = getData(url)
                            soup3 = BeautifulSoup(html3, features='lxml')
                            tr3 = soup3.find_all('tr', {"class": "towntr"})
                            for j in tr3:
                                muted = j.find_all('a')
                                if len(muted) > 0:
                                    print('====================================')
                                    print(muted[-1].string)
                                    html4 = getData(baseUrl2+muted[0]['href'])
                                    soup4 = BeautifulSoup(html4, features='lxml')
                                    tr4 = soup4.find_all('tr', {"class": "villagetr"})
                                    for j in tr4:
                                        muted = j.find_all('td')
                                        print(muted[-1].string)



    #         path = os.path. join(j.get_text())
    #         if not os.path.exists(path):
    #             os.mkdir(path)
    #
    #             path1 = os.path.join(a1[-1].string)
    #             if not os.path.exists(path1):
    #                 os.mkdir(path1)
    # os.chdir(path)



# for i in a2:
#     print(i.get_text())
