#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 3:54 PM
# @Author  : liangk
# @Site    : 
# @File    : task12-2.py
# @Software: PyCharm

import requests
import json
import csv
import openpyxl


def save_json(data):
    with open('juejin.json', 'w') as file:
        json.dump(data, file)


def save_excel(data):
    # 创建表格
    wb = openpyxl.Workbook()
    sheet = wb.active
    # 表头
    poins_header = ['username', 'content']
    sheet.append(poins_header)
    sheet.title = '肥仔'
    # 行数据
    save_list = get_data(data)
    print(save_list)
    print('------')
    for data in save_list:
        sheet.append(data)
    # 保存
    wb.save('juejin.xlsx')


def save_csv(data):
    list_data = get_data(data)
    header = ['username', 'content']
    with open('juejin.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        # 标题
        f_csv.writerow(header)
        # 行数据
        f_csv.writerows(list_data)


def get_data(data):
    points = []
    for point in data:
        point_info = []
        point_info.append(point['user']['username'])
        point_info.append(point['content'])
        points.append(point_info)
    return points


# 程序主入口
if __name__ == '__main__':
    url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?src=web&before&limit=20'
    request = requests.get(url)
    # 判断请求结果，返回数据
    if request.status_code == 200:
        result = request.json()
        point_list = result['d']['list']

    # json文件
    save_json(point_list)
    # CSV文件
    save_csv(point_list)
    # Excel表格
    save_excel(point_list)
