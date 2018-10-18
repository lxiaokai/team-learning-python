#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#主程序入口
if __name__ == '__main__':
    flag = 1
    while True:
        a=int(input("请输入一个数:"))
        if a=="0":
            print("0的数不是素数")
        elif a =="1":
            print("1的数是素数")
        else:
            for i in range(2,a):
                if a%i==0:
                    j=a/i
                    print("{0} 等于{1}*{2},{0}不是素数".format(a,i,j))
                    break
            else:
                print(a,"是一个素数")