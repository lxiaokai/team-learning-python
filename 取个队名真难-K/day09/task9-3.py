#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 4:13 PM
# @Author  : liangk
# @Site    :
# @File    : task9-3.py
# @Software: PyCharm

import os


def recursion_dir(path):
    for files in os.listdir(path):
        print(os.path.join(path, files))
        # 文件 继续递归
        if os.path.isdir(os.path.join(path, files)):
            recursion_dir(os.path.join(path, files))

def walk_dirs():
    '''
    top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
    topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False,
                一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
    onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
    followlinks -- 设置为 true，则通过软链接访问目录。
    '''
    # 注意 top参数的问题,它是包含自己的,所以这里默认不写路径的话,会遍历当前目录下所有的文件,此时可以指定文件夹遍历
    # 完整路径: os.path.abspath('language')
    for root, dirs, files in os.walk('language', topdown=True, followlinks=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


# 程序主入口
if __name__ == '__main__':
    # 遍历的目录
    walk_dirs()
    print('-------------')
    recursion_dir('language')
