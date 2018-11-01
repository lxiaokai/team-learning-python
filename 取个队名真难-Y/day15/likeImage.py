#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import ssl
import re
import os

ssl._create_default_https_context = ssl._create_unverified_context
image_urlList = []
j = 1
def download_img(url):
    request = requests.get(image_urlList[i])
    if request.status_code == 200:
        base_name = os.path.basename(image_urlList[i])
        with open('%s.jpg' % base_name,'wb') as img:
            img.write(request.content)
    else:
        print('error')

def getData(url):
    
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features = 'lxml')
    div = soup.find('div',{"class": "widget d_postlist"})
    image_links = div.find_all('img',{'src': re.compile('https://cuiqingcai.*') })
    for url in image_links:
        image_urlList.append(url['src'])
if __name__ == '__main__':
    url = 'https://cuiqingcai.com/5052.html'
    getData(url)
    print(len(image_urlList))
    for i in range(0,len(image_urlList)):
        download_img(i)
