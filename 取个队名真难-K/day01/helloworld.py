#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 3:42 PM
# @Author  : liangk
# @Site    : 
# @File    : helloworld.py
# @Software: PyCharm

import datetime
import time

# 程序主入口
if __name__ == '__main__':

    print("Hello World!")

    i = 0
    while i < 4:
        nowDate = time.strftime("%Y年%m月%d日 %I:%M:%S")
        print("Hello World! %s" % nowDate)
        i += 1
        time.sleep(1)
