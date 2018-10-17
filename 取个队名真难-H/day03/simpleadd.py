#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#主程序入口
if __name__ == '__main__':
    flag = 1
    while True:
        a=input("请输入一个数字：")
        if a == "q":
            break
        else:
            b=input("请再输入一个数字：")
            pi=3.14
            #计算加法
            sum=float(a)+float(b)
            print('数字 {0} 和 {1} 相加结果为： {2}'.format(a, b, sum))
            #计算减法
            subc=float(a)-float(b)
            print('数字 {0} 和 {1} 相减结果为： {2}'.format(a, b, subc))
            #计算乘法
            mutil=float(a)*float(b)
            print('数字 {0} 和 {1} 相乘结果为： {2}'.format(a, b, mutil))
            #计算除法
            if b=="0":
                print("非法输入,num2不能为0")
            else:
                divi= float(a)/float(b)
                print('数字 {0} 和 {1} 相乘结果为： {2}'.format(a, b, divi))
            #取模
            yu=float(a)%float(b)
            print('数字 {0} 和 {1} 取余结果为： {2}'.format(a, b, yu))
            #计算圆面积
            s=float(pi)*float(a)**2
            print('数字 {0} 半径面积结果为： {1}'.format(a,s))
            #计算圆周长
            c=2 * float(pi) * float(a)
            print('数字 {0} 半径周长结果为： {1}'.format(a, c))
