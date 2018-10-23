#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 4:11 PM
# @Author  : liangk
# @Site    : 
# @File    : task9-2.py
# @Software: PyCharm

import os


def make_dir(dirList):
    i = 0
    for value in dirList:
        i += 1
        # 先判断是否存在文件
        exists = os.path.exists(value)
        if not exists:
            # 不存在,创建目录
            os.mkdir(value)
            print('文件夹创建成功 %s' % os.path.abspath(value))

        # os.chdir() 方法用于改变当前工作目录到指定的路径。
        # 关键点是这个,可以切换目录
        os.chdir(value)

        # 创建txt文件
        with open('index%d.txt' % i, 'w') as file:
            file.write('肥仔肥仔%d' % i)
        print('文件创建成功 %s' % os.path.abspath('index%d.txt' % i))


# 程序主入口
if __name__ == '__main__':
    # dir_path = 'language/python/learn'
    # 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹.
    # os.makedirs(dir_path)
    # 文件夹可以快速建立,但是文件没有,不符合要求
    # 递归删除目录
    # os.removedirs(dir_path)

    # 递归创建文件夹以及目录
    directoryList = ['language', 'python', 'learn']
    make_dir(directoryList)
