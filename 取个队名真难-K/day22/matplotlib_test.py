#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 9:49 AM
# @Author  : liangk
# @Site    : https://blog.csdn.net/qq_34337272/article/details/79555544#3____122
# @File    : matplotlib_test.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np


def func1():
    """画一个基础x-y的坐标轴"""
    x = np.linspace(-1, 1, 50)
    y = 2 * x + 1
    # 定义图像窗口
    plt.figure()
    plt.plot(x, y)
    # 显示图像
    plt.show()


def func2():
    # 绘制普通图像
    x = np.linspace(-1, 1, 50)
    y1 = 2 * x + 1
    y2 = x ** 2

    plt.figure()
    plt.plot(x, y1)
    plt.plot(x, y2, color='red', linewidth=1.0, linestyle=':')

    # 设置坐标轴的取值范围
    plt.xlim((-1, 1))
    plt.ylim((0, 3))

    # 设置坐标轴的lable
    # 标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
    plt.xlabel(u'这是x轴', fontproperties='SimHei', fontsize=14)
    plt.ylabel(u'这是y轴', fontproperties='SimHei', fontsize=14)

    # 设置x坐标轴刻度, 之前为0.25, 修改后为0.5
    # 也就是在坐标轴上取5个点，x轴的范围为0到1所以取2个点之后刻度就变为0.5了
    plt.xticks(np.linspace(0, 1, 2))
    plt.show()


def func3():
    """设置坐标轴的范围, 单位长度, 替代文字"""
    x = np.linspace(-1, 1, 50)
    y = x ** 2
    # 定义图像窗口
    plt.figure()
    # color属性设置颜色，linewidth属性设置线条宽度像素，linestyle属性设置线条样式
    plt.plot(x, y, color='red', linewidth=1, linestyle=':')
    # 使用pyplot.xlim()设置x坐标轴范围
    plt.xlim(-1, 2)
    # 使用pyplot.ylim()设置y坐标轴范围
    plt.ylim(-1, 2)
    # 使用pyplot.xlabel()设置x坐标轴名称
    plt.xlabel('this is X')
    # 使用pyplot.ylabel()设置y坐标轴名称
    plt.ylabel('this is Y')
    # pyplot.xticks()设置x轴刻度
    # pyplot.yticks()设置y轴刻度
    # 显示图像
    plt.show()


# 程序主入口
if __name__ == '__main__':
    func3()
