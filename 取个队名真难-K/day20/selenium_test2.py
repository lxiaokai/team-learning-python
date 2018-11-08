#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 3:40 PM
# @Author  : liangk
# @Site    : 
# @File    : selenium_test2.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 程序主入口
if __name__ == '__main__':
    '''模拟提交提交搜索的功能，首先等页面加载完成，然后输入到搜索框文本，点击提交。'''
    # driver = webdriver.Chrome()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # print(driver.page_source)


    driver1 = webdriver.Chrome()
    driver1.get("http://www.baidu.com/")
    assert "百度" in driver1.title
    elem = driver1.find_element_by_name("wd")
    elem.send_keys("肥仔")
    elem.send_keys(Keys.RETURN)
    print(driver1.page_source)
