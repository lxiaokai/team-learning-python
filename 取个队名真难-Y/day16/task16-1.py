# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ =="__main__":
# 使用Beautiful Soup
# Beautiful Soup 是python的一个HTML和XML的解析库
# 自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码
# 解析器：
# 1.Python标准库 2.lxml HTML解析器 3.lxml XML解析器 4.html5lib
    prinvice = []
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = requests.get(url = url,headers = header )
    request.encoding = 'gbk'
    html = request.text
    soup = BeautifulSoup(html,'lxml')
    for n in soup.find_all(attrs = {'class': 'provincetr'}):
        for m in n:
            if not m.a is None:
                prinvice.append(m.a.get_text())
    print(prinvice)