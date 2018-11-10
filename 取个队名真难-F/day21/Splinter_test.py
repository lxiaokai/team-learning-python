# @time 2018/11/9 16:55
# @Author lhf
from splinter import Browser
from splinter.driver import webdriver

if __name__ == '__main__':
    browser = Browser(driver_name='chrome')
    browser.get('http://www.baidu.com/')
    # 访问 URL
    url = "http://baidu.com"
    browser.visit(url)
    browser.fill('wd', 'splinter - python acceptance testing for web applications')
    # 找到并点击搜索按钮
    button = browser.find_by_xpath('//input[@type="submit"]')
    # 与元素交互
    button.click()
