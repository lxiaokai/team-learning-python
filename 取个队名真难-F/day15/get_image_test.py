# @time 2018/10/31 15:05
# @Author lhf
import base64

import requests
from bs4 import BeautifulSoup
from download_class import MyDownload

def download_page():
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    data = requests.get(str(base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoc2guY29tLw=='), 'utf-8'), headers=headers).content
    return data


if __name__ == '__main__':
    doc = download_page()
    soup = BeautifulSoup(doc, 'html.parser')
    ul = soup.find('ul', class_='cl')  # 下载第一部分图片 6张
    d = MyDownload()
    d.makeDir('img')
    i = 0
    for img in ul.find_all('li', class_='tm02'):
        i += 1
        d.download(img.find('img')['src'], str(i), 'img')  # 获取 img标签下的 src 内容
