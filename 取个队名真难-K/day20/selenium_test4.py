#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 5:07 PM
# @Author  : liangk
# @Site    : 
# @File    : selenium_test4.py
# @Software: PyCharm

from selenium import webdriver
import time

# 程序主入口
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://pythonscraping.com/pages/cookies/login.html')
    # 最大化浏览器
    # driver.maximize_window()
    # 获取元素
    account = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    time.sleep(1)
    # 赋值
    account.send_keys('肥仔')
    time.sleep(1)
    password.send_keys('肥肥')
    # 延迟3秒
    time.sleep(1)
    login_form = driver.find_elements_by_css_selector('input')
    login_form[2].click()
    # 关闭浏览器
    driver.quit()
    # 关闭tab
    # driver.close()


    '''
    单个查找
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    
    一次查找多个元素 (这些方法会返回一个list列表):
    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector

    '''
