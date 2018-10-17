#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 10:42 AM
# @Author  : liangk
# @Site    : 打卡任务
# @File    : task3-1.py
# @Software: PyCharm

import math


def perimeter(r):
    return 2 * r * math.pi


def area(r):
    return math.pi * r * r


# 程序主入口
if __name__ == '__main__':
    x = float(input("数字1:"))
    y = float(input("数字2:"))
    z = x % y
    print("x + y = %f" % (x + y))
    print("x - y = %f" % (x - y))
    print("x * y = %f" % (x * y))
    print("x / y = %f" % (x / y))
    print("x % y =", z)

    radius = input("请输入半径r:")
    print("圆周长：%s" % perimeter(float(radius)))
    print("圆面积：%s" % area(float(radius)))
