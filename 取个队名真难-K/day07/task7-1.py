#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 2:39 PM
# @Author  : liangk
# @Site    : 
# @File    : task7-1.py
# @Software: PyCharm


def hello():
    print('hello world')


def getString():
    return 'python'


def getInt():
    return 110


def oneParameter(a):
    return a + 1



# 程序主入口
if __name__ == '__main__':
    # def 函数名（参数列表）:
    #       函数体

    # 调用函数
    hello()

    string = getString()
    print(string)

    print(getInt())

    print(oneParameter(1))
    '''
        上面只是简单的举例说明一下函数的使用,比如什么默认参数之类的就不举例了,使用方式差不多
    '''
