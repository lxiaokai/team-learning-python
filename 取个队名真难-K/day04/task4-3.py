#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 2:48 PM
# @Author  : liangk
# @Site    : 
# @File    : task4-3.py
# @Software: PyCharm


# 程序主入口
if __name__ == '__main__':
    # 定义1
    dict = {'a': 'python', 'b': 'python', 'c': 'python'}
    print('定义字典: ', dict)
    # 定义2
    dict1 = {'d': dict, 'e': 'test'}
    print('字典嵌套定义字典: ', dict1)
    # 定义3
    list = ['1', 2, 12.3]
    dict2 = {'d': list, 'e': 'test'}
    print('数组嵌套定义字典: ', dict2)

    print('---------取值-----------')
    print('取值:', dict['a'])

    print('修改前字典: ', dict)
    dict['a'] = 'wo'
    print('修改后字典: ', dict)

    dict3 = {'a': 'python', 'b': 'python', 'c': 'python'}
    # 请空字典
    dict.clear()
    # 此处打印他,只是空,不会报错
    print('字典清空了,空字典,可以调用使用它', dict)

    dict4 = {'a': 'python', 'b': 'python', 'c': 'python'}
    # 请空字典
    del dict4
    # 调用,会报错 NameError: name 'dict4' is not defined
    print('字典删除了,不可以调用和使用它')

    dict5 = {'a': 'python1', 'b': 'python2', 'c': 'python3'}
    print('获取所有的kes', dict5.keys())
    for key in dict5.keys():
        print(key)
    print('获取所有的value', dict5.values())
    for value in dict5.values():
        print(value)

    print('字典长度: ', len(dict5))
    print('字典str: ', str(dict5))
    print('字典类型: ', type(dict5))

    print('字典元组: ', dict5.items())
    # 元组
    for (key, value) in dict5.items():
        print(key, value)

    dict6 = dict5.copy()
    print(dict6)

    dict7 = {'Name': 'fat boy', 'Age': 25}
    dict8 = {'Sex': 'man'}

    dict7.update(dict8)
    print("更新字典 dict : ", dict7)

    dict7.pop('Age')
    print("删除后字典 dict : ", dict7)

    # seq -- 字典键值列表。
    # value -- 可选参数, 设置键序列（seq）的值。
    seq = ('name', 'age', 'sex')
    dict9 = {}
    dict10 = {}
    dict9 = dict9.fromkeys(seq)
    print("新的字典为 : %s" % str(dict9))

    dict10 = dict10.fromkeys(seq, 10)
    print("新的字典为 : %s" % str(dict10))
