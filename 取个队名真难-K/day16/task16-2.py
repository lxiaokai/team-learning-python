#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 6:06 PM
# @Author  : liangk
# @Site    : 
# @File    : task16-2.py
# @Software: PyCharm


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
# 这种Tag类型。Tag具有一些属性，比如string属性，调用该属性，可以得到节点的文本内容
print(type(soup.title))
print(soup.title.string)
print(soup.head)
# 发现结果是第一个p节点的内容，后面的几个p节点并没有选到。
# 也就是说，当有多个节点时，这种选择方式只会选择到第一个匹配的节点，
# 其他的后面节点都会忽略。
print(soup.p)
