#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:31 AM
# @Author  : liangk
# @Site    : 输入一个数，判断该数是不是素数
# @File    : task4-1.py
# @Software: PyCharm


# 程序主入口
if __name__ == '__main__':

    # 素数又称质数，有无限个
    # 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。

    while True:
        num = int(input("请输入一个整数："))
        if num > 1:
            if num == 2:
                print("2是素数")
            for i in range(2, num):
                if num % i == 0:
                    print("不是素数")
                    break
                if num % i != 0 and num != 1:
                    print("%d是素数" % num)
                    break
        else:
            print("只有当输入的整数是大于等于2时，题目才有意义")
