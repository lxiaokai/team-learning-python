# @time 2018/11/10 15:07
# @Author lhf
import os
import time

import requests
from selenium import webdriver


# 进入天猫首页
# 输入一个商品关键词进行搜索（商品关键词自己定）
# 然后爬取商品信息（信息包含：商品图片，价格，购买人数，名称，所属店铺，店铺地点，商品链接……）
search_key = '裤子'


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


def download(url, name, save_path):
    # 名称
    # url_data = parse.urlparse(url=url)
    # # 请求参数
    # url_param = parse.parse_qs(url_data.query)
    #
    # url = url_param['src'][0]
    # 扩展名
    try:
        ext_name = url.split('.')[-1]

        save_name = name + '.' + ext_name
        img_path = os.path.join(save_path, save_name)
        with open(img_path, 'wb') as o:
            data = requests.get(url)
            o.write(data.content)
    except:
        pass



if __name__ == '__main__':
    product_json = {'title': '', 'price': '', 'status': '', 'shop': '', 'imgUrl': '', }
    driver = webdriver.Chrome()
    driver.get("https://www.tmall.com/")
    print(driver.title)
    input = driver.find_element_by_xpath("//input[@id='mq']")  # 输入框
    search_button = driver.find_element_by_xpath("//button[@type='submit']")  # 搜索按钮
    input.send_keys(search_key)
    search_button.click()  # 点击搜索按钮


    # for i in range(0, 3):
    driver.execute_script("window.scrollTo(0, 500)") # 试着滑动一下，看看是否多了一些图片链接
    driver.implicitly_wait(3)

    item_list = driver.find_elements_by_xpath("//div[@class='product-iWrap']")
    print(len(item_list))

    first_path = 'tmall'
    makeDir(first_path)
    for item in item_list:
        try:
            price = item.find_element_by_css_selector(".productPrice em").text
            imgUrl = item.find_element_by_css_selector(".productImg-wrap img").get_attribute('src')
            title = item.find_element_by_css_selector(".productTitle a").text
            shop = item.find_element_by_css_selector(".productShop a").text
            status = item.find_element_by_css_selector(".productStatus span").text
            product_json['title'] = title
            product_json['price'] = price
            product_json['status'] = status
            product_json['shop'] = shop
            product_json['imgUrl'] = imgUrl

            print(product_json)

            save_path = first_path + "/" + title
            makeDir(save_path)  # 创建以标题命名的文件夹
            download(imgUrl, title, save_path)
            with open(save_path + "/" + title + ".json", 'w', encoding='utf-8') as f:
                f.write(product_json.__str__())

        except Exception as e:  # 有的是广告item,所以拿不到一些数据，索性抛异常不存它了
            pass

    driver.close()
