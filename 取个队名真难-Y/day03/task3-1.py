# -*- coding: utf-8 -*-
import math
if __name__ =="__main__":
    a = int (input()) # python中input函数返回的是一个字符串，而只有通过int进行强制转换
    b = int (input())
    r = int (input())
    print('a+b=',a+b)
    print('a-b=',a-b)
    print('a*b=',a*b)
    if b != 0:
        print('a/b=',a/b)
    else :
        print('除数为0！')
    print('圆的周长为：',2 * math.pi * r)
    print('圆得面积为：',math.pi * math.pow(r,2))
    