# @time 2018/11/8 9:52
# @Author lhf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def init():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


if __name__ == '__main__':
    # init()
    driver = webdriver.Chrome()
    driver.get("https://juejin.im/timeline")
    print(driver.title)
    ul=driver.find_element_by_xpath("//ul[@class='entry-list']") #内容列表
    # title=driver.find_elements_by_class_name("title")
    title=ul.find_elements_by_xpath("//a[@class='title']") #文章标题

    # div=ul.find_elements_by_xpath("//div[@class='user-popover-box']")
    user = ul.find_elements_by_css_selector(".user-popover-box a")#文章作者
    print(len(title))
    # print(len(div))
    print(len(user))
    for t in title:
        print("作者："+user[title.index(t)].text,",内容:"+t.text)
    driver.close()
