#!/usr/bin/env python
#  -*- coding: utf-8 -*-
# 主程序入口
if __name__ == '__main__':
    flag = 1
    while True:
        val = input("请输入一个方式；1加，2减，3乘法，4除:")
        if val == "q":
            break
        else:
            num1 = input("请输入一个数字：")
            num2 = input("请输入一个数字")
            if val == "1":
                sum = float(num1) + float(num2)
                print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
            elif val == "2":
                subctr = float(num1) - float(num2)
                print('数字 {0} 和 {1} 相减结果为： {2}'.format(num1, num2, subctr))
            elif val == "3":
                mutil = float(num1) * float(num2)
                print('数字 {0} 和 {1} 相乘结果为： {2}'.format(num1, num2, mutil))
            elif val == "4":
                if num2 == "0":
                    print("非法输入,num2不能为0")
                else:
                    divi = float(num1) / float(num2)
                    print('数字 {0} 和 {1} 相乘结果为： {2}'.format(num1, num2, divi))
    else:
        print("非法输入,error")
