#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 4:43 PM
# @Author  : liangk
# @Site    : 
# @File    : getStreetAgency_1.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
from urllib import parse
import datetime

origin_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    request.encoding = 'gbk'
    if request.status_code == 200:
        html = request.content
    return html


def get_province(html):
    # print('获取省份~')
    soup = BeautifulSoup(html, 'lxml')

    province_tr = soup.find_all(class_='provincetr')
    for province_info in province_tr:
        a = province_info.find_all('a')
        for a_info in a:
            '''
            甘肃省 62.html
            <a href="63.html">青海省<br/></a>
            青海省 63.html
            <a href="64.html">宁夏回族自治区<br/></a>
            '''
            # 这里a_info 只有一个,所以可以这样取值,
            # 下面获取市的试试,是返回两个以上,不能这样取
            province_name = a_info.get_text()
            province_href = a_info['href']
            print(province_name, province_href)
            get_city(province_href)

    # 等价于下面的操作
    # province_list = soup.select('.provincetr a')
    # for province_info in province_list:
    #     province_name = province_info.get_text()
    #     province_href = province_info.attrs['href']
    #     print(province_name, province_href)
    #     get_city(province_href)


def get_city(url):
    # print('获取市~')
    province_url = parse.urljoin(origin_url, url)
    # 再次解析
    html = get_html(province_url)
    soup = BeautifulSoup(html, 'lxml')

    city_tr = soup.find_all(class_='citytr')
    for city_info in city_tr:
        a_info = city_info.find_all('a')
        city_name = a_info[1].get_text()
        city_code = a_info[0].get_text()
        city_url = a_info[0].attrs['href']
        print(city_name, city_code, city_url)

        # 获取县级
        get_county(city_url)
        '''
        北京市 11.html
        <a href="11/1101.html">110100000000</a>
        <a href="11/1101.html">市辖区</a>
        天津市 12.html
        <a href="12/1201.html">120100000000</a>
        <a href="12/1201.html">市辖区</a>
        河北省 13.html
        <a href="13/1301.html">130100000000</a>
        <a href="13/1301.html">石家庄市</a>
        <a href="13/1302.html">130200000000</a>
        <a href="13/1302.html">唐山市</a>
        <a href="13/1303.html">130300000000</a>
        '''
    # 等价于这个
    # city_list = soup.select('.citytr')
    # for city_info in city_list:
    #     a_info = city_info.find_all(name='a')
    #     city_name = a_info[1].get_text()
    #     city_code = a_info[0].get_text()
    #     city_url = a_info[0].attrs['href']
    # print(city_name, city_code, city_url)


def get_county(url):
    """县区"""
    city_url = parse.urljoin(origin_url, url)
    # 再次解析
    html = get_html(city_url)
    soup = BeautifulSoup(html, 'lxml')
    county_list = soup.select('.countytr')
    for county_info in county_list:

        a_info = county_info.find_all('a')
        '''
        [<a href="01/120119.html">120119000000</a>, <a href="01/120119.html">蓟州区</a>]
        []
        '''
        # 这里需要判断一下是否都有值
        if a_info:
            county_name = a_info[1].get_text()
            county_code = a_info[0].get_text()
            county_url = a_info[0].attrs['href']
            print(county_name, county_code, county_url)
            # 获取乡镇信息
            get_town(city_url, county_url)
        else:
            td_info = county_info.find_all(name='td')
            county_name = td_info[1].get_text()
            county_code = td_info[0].get_text()
            county_url = ''
            print(county_name, county_code, county_url)


def get_town(url, now_url):
    """办事处"""
    county_url = parse.urljoin(url, now_url)
    # 再次解析
    html = get_html(county_url)
    soup = BeautifulSoup(html, 'lxml')
    town_list = soup.select('.towntr')
    for town_info in town_list:
        a_info = town_info.find_all(name='a')
        town_name = a_info[1].get_text()
        town_code = a_info[0].get_text()
        town_url = a_info[0].attrs['href']
        print(town_name, town_code, town_url)
        # 获取村级信息
        # get_village(county_url, town_url)



def get_village(url, now_url):
    '''居委会'''
    town_url = parse.urljoin(url, now_url)
    # 再次解析
    html = get_html(town_url)
    soup = BeautifulSoup(html, 'lxml')
    village_list = soup.select('.villagetr')
    for village_info in village_list:
        a_info = village_info.find_all(name='td')
        village_name = a_info[2].get_text()
        village_code = a_info[0].get_text()
        village_url = ''
        print(village_name, village_code, village_url)


# 程序主入口
if __name__ == '__main__':

    start_time = datetime.datetime.now()
    print(start_time)
    print('开始请求~')
    html = get_html(origin_url)
    print('请求完毕!')

    # 省份
    get_province(html)

    end_time = datetime.datetime.now()

    print((end_time - start_time).seconds)
