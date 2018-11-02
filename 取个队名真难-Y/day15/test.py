#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    url = 'https://cuiqingcai.com/5548.html'
    print(urlopen(url).read())