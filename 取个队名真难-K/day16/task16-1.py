#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 10:42 AM
# @Author  : liangk
# @Site    : 打卡任务
# @File    : task3-1.py
# @Software: PyCharm

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')


# 查找class = panel的所有, 再查找 class = panel-heading 的
# 也可以直接精确到后面的 .panel-heading
print(soup.select('.panel .panel-heading'))

# 选择 <ul> 元素内部的所有 <li> 元素。
print(soup.select('ul li'))

# 嵌套选择。例如，先选择所有ul节点，再遍历每个ul节点，选择其li节点
for ul in soup.select('ul'):
    print(ul.select('li'))


# 选择 id="list-2" 的所有元素。 然后再选择 class="element" 的所有元素。
# print(soup.select('#list-2 .element'))

# 输出了列表中元素的类型。可以看到，类型依然是Tag类型。
print(type(soup.select('ul'))) #<class 'list'
print(type(soup.select('ul')[0])) #<class 'bs4.element.Tag'>

# 获取属性
# 直接传入中括号和属性名，以及通过attrs属性获取属性值，都可以成功
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
# list-1
# list-1
# list-2
# list-2

for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
