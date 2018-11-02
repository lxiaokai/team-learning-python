#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

book_nameList = []
book_dateList = []
def getData(url):

    r = urlopen(url)
    html = r.read()
    soup = BeautifulSoup(html, features = 'lxml')
    div = soup.find('div',{"class": "widget d_postlist"})
    span = div.find_all('span',{'class': 'text'})
    # date = div.find_all('span',{'class': 'muted'})
    for s in span:
        book_nameList.append(s.get_text())
    #for d in date:
        #book_dateList.append(d.get_text())

if __name__ == '__main__':
    url = 'https://cuiqingcai.com/5548.html'
    r = urlopen(url)
    html = r.read()
    print(html)
    exit()
    # getData(url)
    #for i in range(0,len(book_nameList)):
        #with open('%s.txt' % book_nameList[i],'wb') as file:
            #file.write('标题：%s\n' % book_nameList[i])
            
