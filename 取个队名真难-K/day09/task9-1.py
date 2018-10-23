#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 2:16 PM
# @Author  : liangk
# @Site    : 
# @File    : task9-1.py
# @Software: PyCharm

import functools


def log(func):
    @functools.wraps(func)
    def before(number):
        print('请稍等, 肥仔正在判断!')
        return func(number)

    return before


@log
def is_prime(x):
    if x > 1:
        if x == 2:
            print('%d 是素数' % x)
            return
        for i in range(2, x):
            if x % i == 0:
                break
            if x % i != 0 and x != 1:
                print('%d 是素数' % x)
                break
    else:
        print('肥仔别闹,输入2以上的数字')


# 程序主入口
if __name__ == '__main__':

    while True:
        num = int(input('请输入数字:'))
        is_prime(num)
