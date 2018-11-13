#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 9:44 AM
# @Author  : liangk
# @Site    : 
# @File    : selenuim_JD.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('start-maximized')
# driver = webdriver.Chrome(chrome_options=chrome_options)
max_page = 5
search_key = '衬衫'


def initialize():

    try:
        driver.get('https://www.jd.com/')
        wait = WebDriverWait(driver, 10)
        # driver.maximize_window()
    except Exception as e:
        print('打开异常')
        driver.quit()
    # 获取搜素框
    searchInput = driver.find_element_by_xpath("//input[@id='key']")
    # 获取搜素按钮
    searchBtn = driver.find_element_by_xpath("//button[@class='button']")
    # 赋值
    searchInput.send_keys(search_key)
    # 点击
    searchBtn.click()
    time.sleep(4)


def get_good_info():
    '''获取商品信息'''
    # driver.execute_script("window.scrollTo(0, 500)") # 试着滑动一下，看看是否多了一些图片链接
    # driver.implicitly_wait(3)
    for x in range(1, 11, 2):
        time.sleep(1)
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

    try:
        good_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='J_goodsList']"))
        )
        good_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='gl-i-wrap']"))
        )
    except Exception as e:
        print('异常啦')
        driver.quit()
    finally:
        print('第%s页,加载完毕了~' % (page + 1))
    for good in good_list:
        good_name = good.find_element_by_css_selector(".p-name em").text
        price = good.find_element_by_css_selector(".p-price i").text
        shop = good.find_element_by_css_selector(".p-shop span a").text
        imgUrl = good.find_element_by_css_selector(".p-img a img").get_attribute('src')
        if not imgUrl:
            lazy_imgurl = good.find_element_by_css_selector(".p-img a img").get_attribute('data-lazy-img')
            imgUrl = 'https:%s' % lazy_imgurl
        print('商品名:', good_name, '价格: ¥', price, '店铺:', shop, '图片地址:', imgUrl, '\n')
        '''这里可以进行数据储存和下载图片啦~'''
    if page < max_page - 1:
        next_a = driver.find_element_by_class_name('pn-next')
        next_a.click()


# 程序主入口
if __name__ == '__main__':
    start_time = datetime.datetime.now()

    initialize()
    for page in range(0, max_page):
        get_good_info()
    driver.quit()

    end_time = datetime.datetime.now()
    print('耗时: ', (end_time - start_time).seconds)
