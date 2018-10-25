# -*- coding: utf-8 -*-
import requests
if __name__ =="__main__":
    r = requests.get('https://www.douban.com')
    print(r.status_code)
    # print(r.text)
    # 对于带参数URL，传入一个dict作为param参数
    r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
    print(r.url)
    # requests 自动检测编码
    print(r.encoding)
    # 无论响应是文本还是二进制，都可以用content 属性获得bytes对象
    print(r.content)