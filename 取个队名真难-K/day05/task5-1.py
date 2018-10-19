#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 11:31 AM
# @Author  : liangk
# @Site    : 
# @File    : task5-1.py
# @Software: PyCharm


primeList = []
primeDict = {}


def is_prime(num):
    if num > 1:
        if num == 2:
            primeList.append(num)
        for i in range(2, num):
            if num % i == 0:
                break
            if num % i != 0 and num != 1:
                primeList.append(num)
                break
    else:
        print("list中有小于2的数字,全部大于等于2时，题目才有意义")
    primeDict['素数'] = primeList
    return primeDict


# 程序主入口
if __name__ == '__main__':
    list = [1, 2, 3, 5, 6, 7]
    for i in list:
        is_prime(i)

    print(primeList)
    print(primeDict)
