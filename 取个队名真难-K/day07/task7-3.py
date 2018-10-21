#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 2:49 PM
# @Author  : liangk
# @Site    : 
# @File    : task7-3.py
# @Software: PyCharm

import os

# 程序主入口
if __name__ == '__main__':

    # 查看当前所在路径。
    print(os.getcwd())

    # 查看路径先的所有文件
    print(os.listdir(os.getcwd()))

    # 返回path的绝对路径
    print(os.path.abspath('.'))
    print(os.path.abspath('..'))

    # 将路径分解为(文件夹,文件名)，
    # 返回的是元组类型。可以看出，若路径字符串最后一个字符是\,则只有文件夹部分有值；
    # 若路径字符串中均无\,则只有文件名部分有值。若路径字符串有\，且不在最后，则文件夹和文件名均有值。
    # 且返回的文件夹的结果不包含\.
    # os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除
    print(os.path.split('/Users/liangk/Documents/Team-learning-python/取个队名真难-K/task7-1.py'))

    # os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'
    print(os.path.dirname('/Users/liangk/Documents/Team-learning-python/取个队名真难-K'))

    # os.path.basename(path):返回path中的文件名
    print(os.path.basename(os.getcwd()))

    # os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
    #
    #  os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
    #
    #  os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数。
    print(os.path.getmtime(os.getcwd()))
    print(os.path.getatime(os.getcwd()))
    print(os.path.getctime(os.getcwd()))

    #   os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0。
    print(os.path.getsize(os.getcwd()))

    #  os.path.exists(path):文件或文件夹是否存在，返回True 或 False
    print(os.path.exists('/Users/liangk/Documents/Team-learning-python/取个队名真难-K/day07/task7-3.py'))

    '''
        参考资料:
            https://www.cnblogs.com/yufeihlf/p/6179547.html
            http://www.runoob.com/python3/python3-os-file-methods.html
    '''
