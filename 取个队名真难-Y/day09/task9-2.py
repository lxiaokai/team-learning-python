# -*- coding: utf-8 -*-
import os
if __name__ =="__main__":
    # print(os.uname())
    # os模块的某些函数是跟操作系统相关的
    # 环境变量
    # 在操作系统中定义的环境变量，全部保存在os.environ里
    # print(os.environ)
    # 获取某个环境变量的值 os.enbiron.get('key')
    # print(os.environ.get('PATH'))
    # 操作文件和目录
    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/','language')
    # os.mkdir('language')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/language','python')
    # os.mkdir('language/python')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/language/python','learn')
    # os.mkdir('./language/python/learn')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09','inedx.txt')
    # os.mkdir('index.txt')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/language','inedx.txt')
    # os.mkdir('language/index.txt')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/language/python','inedx.txt')
    # os.mkdir('language/python/index.txt')
    # os.path.join('/Users/yuhong/team-learning-python/取个名字真难-Y/day09/language/python/learn','inedx.txt')
    # os.mkdir('./language/python/learn/index.txt')
    for root, dirs ,files in os.walk('.',topdown=False):
        for name in files:
            print(os.path.join(root,name))
        for name in dirs:
            print(os.path.join(root,name))


