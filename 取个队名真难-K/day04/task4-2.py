#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 2:22 PM
# @Author  : liangk
# @Site    :
# @File    : task4-2.py
# @Software: PyCharm


# for的一些基本使用
def forMethods():
    for i in 'python':
        print(i)

    for i1 in ['python1', 'python2', 'python3']:
        print(i1)

    for i2 in range(1, 3):
        # 1
        # 2
        print(i2)

    list = ['python1', 'python2', 'test1', 'python3', 'test2']
    for i3 in range(len(list)):
        print(list[i3])
        if list[i3] == 'test1':
            print('测试~')
            break


# while 基本使用
def whileMethods():
    count = 0
    while count < 9:
        print(count)
        count = count + 1

    print("----------------")
    count1 = 0
    while count1 < 5:
        print(count1)
        if count1 == 3:
            break
        count1 = count1 + 1


# 程序主入口
if __name__ == '__main__':
    print('-------------forMethods---------------')
    forMethods()
    print('-------------whileMethods---------------')
    whileMethods()
