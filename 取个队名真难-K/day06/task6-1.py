#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 6:36 PM
# @Author  : liangk
# @Site    : 
# @File    : task6-1.py
# @Software: PyCharm


def fib(number):
    n, a, b = 0, 0, 1
    while n < number:
        yield b
        a, b = b, a + b
        n = n + 1


# 程序主入口
if __name__ == '__main__':
    num = int(input('请输入数字:'))
    num_list = []
    for i in fib(num):
        num_list.append(i)
    print(num_list)
