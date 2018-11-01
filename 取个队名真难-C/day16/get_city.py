#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用BeautifulSoup爬取省、市、区、街道、办事处五级地址
author: gxcuizy
date: 2018-11-01
"""

import requests
from bs4 import BeautifulSoup
from urllib import parse


class GetCity(object):
    """爬取国家统计局省、市、区、街道、办事处五级地址"""
    # 地址
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'

    def __init__(self):
        """初始化属性"""
        pass

    def get_html(self, url):
        """请求html页面信息"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        request = requests.get(url=url, headers=header)
        request.encoding = 'gbk'
        html = request.text
        return html

    def get_city(self, origin_url, now_url):
        """获取市级地址信息"""
        province_url = parse.urljoin(origin_url, now_url)
        # 解析市级的html
        print('开始解析市级信息……')
        html = self.get_html(province_url)
        soup = BeautifulSoup(html, 'lxml')
        city_list = soup.select('.citytr')
        for city_info in city_list:
            a_info = city_info.find_all(name='a')
            city_name = a_info[1].get_text()
            city_code = a_info[0].get_text()
            city_url = a_info[0].attrs['href']
            print(city_name, city_code, city_url)
            # 获取县区信息
            self.get_county(province_url, city_url)
        print('市级解析结束！')

    def get_county(self, origin_url, now_url):
        """获取县、区级地址信息"""
        city_url = parse.urljoin(origin_url, now_url)
        # 解析县区的html
        print('开始解析县/区级信息……')
        html = self.get_html(city_url)
        soup = BeautifulSoup(html, 'lxml')
        county_list = soup.select('.countytr')
        for county_info in county_list:
            a_info = county_info.find_all(name='a')
            if a_info:
                county_name = a_info[1].get_text()
                county_code = a_info[0].get_text()
                county_url = a_info[0].attrs['href']
                print(county_name, county_code, county_url)
                # 获取乡镇信息
                self.get_town(city_url, county_url)
            else:
                td_info = county_info.find_all(name='td')
                county_name = td_info[1].get_text()
                county_code = td_info[0].get_text()
                county_url = ''
                print(county_name, county_code, county_url)
        print('县/区级解析结束！')

    def get_town(self, origin_url, now_url):
        """获取乡镇地址信息"""
        county_url = parse.urljoin(origin_url, now_url)
        # 解析县区的html
        print('开始解析乡镇级信息……')
        html = self.get_html(county_url)
        soup = BeautifulSoup(html, 'lxml')
        town_list = soup.select('.towntr')
        for town_info in town_list:
            a_info = town_info.find_all(name='a')
            town_name = a_info[1].get_text()
            town_code = a_info[0].get_text()
            town_url = a_info[0].attrs['href']
            print(town_name, town_code, town_url)
            # 获取村级信息
            self.get_village(county_url, town_url)
        print('乡镇级解析结束！')

    def get_village(self, origin_url, now_url):
        """获取村级地址信息"""
        town_url = parse.urljoin(origin_url, now_url)
        # 解析县区的html
        print('开始解析村级信息……')
        html = self.get_html(town_url)
        soup = BeautifulSoup(html, 'lxml')
        village_list = soup.select('.villagetr')
        for village_info in village_list:
            a_info = village_info.find_all(name='td')
            village_name = a_info[2].get_text()
            village_code = a_info[0].get_text()
            village_url = ''
            print(village_name, village_code, village_url)
        print('村级解析结束！')

    def run(self):
        """执行入口"""
        # 解析省份的html
        print('开始解析省份信息……')
        html = self.get_html(self.url)
        soup = BeautifulSoup(html, 'lxml')
        province_list = soup.select('.provincetr a')
        for province_info in province_list:
            province_name = province_info.get_text()
            province_url = province_info.attrs['href']
            print(province_name, province_url)
            # 爬取市级信息
            self.get_city(self.url, province_url)
        print('省份解析结束！')


# 程序主入口
if __name__ == '__main__':
    # 实例化执行
    print('开始执行……')
    city = GetCity()
    city.run()
    print('程序执行结束！')
