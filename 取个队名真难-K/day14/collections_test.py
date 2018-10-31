#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 9:26 AM
# @Author  : liangk
# @Site    : 
# @File    : collections_test.py
# @Software: PyCharm

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

# 程序主入口
if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, 22)
    print('Point:', p.x, p.y)

    q = deque(['a1', 'b1', 'c1'])
    q.append('x')
    q.appendleft('y')
    print(q)

    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print('dd[\'key1\'] =', dd['key1'])
    print('dd[\'key2\'] =', dd['key2'])

    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
