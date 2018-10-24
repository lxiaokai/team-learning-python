# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'yuzuru'

import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s!' % args[1])
    else:
        print('TOO Many')

if __name__ =="__main__":
    # 按目录组织模块的方法，称为包
    # 每个包目录下都有会有一个__init.py__文件，这个文件必须存在，否则就会把这个目录当做普通目录
    # __init__.py 可以是空文件
    # 可以有多级目录，组成多级层次的包结构
    test()
    # 正常的函数和变量名是公开的(public)，可以直接引用
    # _xxx和__xxx是非公开的
    # 安装第三方模块，通过包管理工具pip完成的