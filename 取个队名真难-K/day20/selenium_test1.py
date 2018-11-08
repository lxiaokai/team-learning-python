#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 3:24 PM
# @Author  : liangk
# @Site    : 
# @File    : selenium_test1.py
# @Software: PyCharm

from selenium import webdriver

# 程序主入口
if __name__ == '__main__':
    '''打开浏览器'''
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')
