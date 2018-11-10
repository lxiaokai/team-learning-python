#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 3:52 PM
# @Author  : liangk
# @Site    : 
# @File    : selenium_test3.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
测试用例类继承自unittest.TestCase。继承TestCase类是告诉unittest模块这是一个测试用例的方法。
setUp是初始化的一部分，这个方法将在你要在这个测试用例类中编写的每个测试函数之前调用。
测试用例方法应始终以字符测试开始。每个测试方法后都会调用tearDown方法。这是一个执行所有清理操作的地方。
您也可以调用quit方法而不是close。退出将退出整个浏览器，而close将关闭一个选项卡，
但如果它是唯一打开的选项卡，默认情况下大多数浏览器将完全退出。


测试用例是继承了unittest.TestCase类，继承这个类表明这是一个测试类.setUp方法是初始化的方法，
这个方法会在每个测试类中自动调用。每一个测试方法命名都有规范，必须以test开头，会自动执行。
最后的tearDown方法会在每一个测试方法结束之后调用。这相当于最后的分构方法。在这个方法里写的是闭方法，
你还可以写quit方法。不过close方法相当于关闭了这个TAB选项卡，然而quit是退出了整个浏览器。
当你只开开了一个TAB选项卡的时候，关闭的时候也会将整个浏览器关闭。
'''

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_BaiDu_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        # self.assertIn("百度", driver.title)
        elem = driver.find_element_by_name("q")
        # 向文本输入内容
        elem.send_keys("肥仔")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        '''close方法相当于关闭了这个TAB选项卡，然而quit是退出了整个浏览器'''
        self.driver.close()


# 程序主入口
if __name__ == '__main__':
    unittest.main()

    '''
    <input type="text" name="passwd" id="passwd-id" />
    
    获取输入框
    element = driver.find_element_by_id("passwd-id")
    element = driver.find_element_by_name("passwd")
    element = driver.find_elements_by_tag_name("input")
    element = driver.find_element_by_xpath("//input[@id='passwd-id']"
    xpath的时候还需要注意的是，如果有多个元素匹配了xpath，它只会返回第一个匹配的元素。如果没有找到，那么会抛出NoSuchElementException的异常。
    '''

    '''
    输入文本内容
    element.send_keys("some text")
    
    
    Keys这个类来模拟点击某个按键。
    element.send_keys("and some", Keys.ARROW_DOWN)
    '''
