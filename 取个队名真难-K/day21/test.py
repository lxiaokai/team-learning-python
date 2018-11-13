#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 3:29 PM
# @Author  : liangk
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import time
from selenium import webdriver  # 导入webdriver包
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
time.sleep(2)  # 暂停2秒钟
driver.get("https://www.baidu.com/")  # 通过get()方法，打开一个url站点
time.sleep(2)  # 暂停2秒钟
try:
    inputText = driver.find_element_by_id("kw")  # 获取用户名元素文本框
    inputText.send_keys("selenuim")  # 输入账号内容
except Exception as e:
    print("Exception found", format(e))
try:
    time.sleep(5)  # 暂停5秒
    # currentWin=driver.current_window_handle#获取当前窗口
    # print(currentWin)
    buttonget = driver.find_element_by_id("su")  # 获取按钮
    # print("button to get class successful")
    buttonget.click()  # 跳转页面
    time.sleep(10)  # 暂停5秒
    sreach_window = driver.current_window_handle
    driver.find_element_by_xpath("/html/body/div/div[2]/div/a").click()
    # no=driver.find_element_by_xpath("//*[@id='s_tab']/div/a2").get_attribute("href")
    # str=driver.find_element_by_xpath('//*[@id="msgpid"]').is_displayed()
    # print("判断标签是否存在输出内容:"+str)
    # print("success to login")
    # if not str =='':
    #     print("登录失败")
    time.sleep(10)
except Exception as e:
    print("Exception found", format(e))
# print("success to login")
driver.quit()
