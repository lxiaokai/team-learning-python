#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 6:13 PM
# @Author  : liangk
# @Site    : 
# @File    : task11-4.py
# @Software: PyCharm

import csv

# 程序主入口
if __name__ == '__main__':
    # csv 写入
    stu1 = ['fat', 26]
    stu2 = ['boy', 17]
    # 写文件
    out = open('test_csv.csv', 'w', newline='')
    # 设定写入模式
    csv_write = csv.writer(out, dialect='excel')
    # 写入具体内容
    csv_write.writerow(stu1)
    csv_write.writerow(stu2)

    print("write over")

    csv_file = csv.reader(open('test_csv.csv', 'r'))
    print(csv_file)

    # 读取文件内容
    # with open("test_csv.csv", "r", encoding="utf-8") as f:
    #     reader = csv.reader(f)
    #     rows = [row for row in reader]
    #     print(rows)
