#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 11:06 AM
# @Author  : liangk
# @Site    : 
# @File    : task3-2.py
# @Software: PyCharm


# 程序主入口
if __name__ == '__main__':

    var1 = 10         # 表示整型,Python3 没有Python2的Long
    var2 = 12.34      # 表示浮点型
    var3 = 123j       # 复数
    var4 = 123 + 45j  # 复数：复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示
    print(var1)
    print(var2)
    print(var3)
    print(var4)
    print(var3 + var4)

    print("")
    print("----------string----------")
    str = "python"
    str1 = 'python1'
    str2 = 'python2'
    print(str)
    print(str1)
    print(str2)
    print(str)             # 输出字符串
    print(str[0:-1])       # 输出第一个到倒数第二个的所有字符
    print(str[0])          # 输出字符串第一个字符
    print(str[2:5])        # 输出从第三个开始到第五个的字符
    print(str[2:])         # 输出从第三个开始的后的所有字符
    print(str * 2)         # 输出字符串两次
    print(str + "TEST")    # 连接字符串

    print("")
    print("----------list----------")
    list = ['Python', 'Python1', 'Python2', 'Python3']
    list1 = ['fat boy', 'fat']
    print(list)
    print(list)            # 输出完整列表
    print(list[0])         # 输出列表第一个元素
    print(list[1:3])       # 从第二个开始输出到第三个元素
    print(list[2:])        # 输出从第三个元素开始的所有元素
    print(list[-2])        # 从后面数回来的第二个，后面数的时候下标是1开始，前面是0开始
    print(list[-3:])       # 从后面数回来的第3个之后所有元素
    print(list[-3:-1])     # 从后面数回来的第3个到从后面数回来第一个元素之间的所有元素
    print(list * 2)        # 输出两次列表
    print(list + list1)    # 连接列表

    print("")
    print("----------tuple----------")
    tuple = ( 'Python', 123, 1.23, 'Python2', 12.3)
    tuple1 = (123, 'Python3')

    print (tuple)             # 输出完整元组
    print (tuple[0])          # 输出元组的第一个元素
    print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
    print (tuple[2:])         # 输出从第三个元素开始的所有元素
    print (tuple1 * 2)        # 输出两次元组
    print (tuple + tuple1)    # 连接元组
