# -*- coding: utf-8 -*-
if __name__ =="__main__":
    n = 1
    a = int(input())
    if a > 1:
        while n < a:
            n = n + 1
            if a % n == 0:
                break
        if(n == a):
            print('是素数')
        else:
            print('不是素数')
    else:
        print('输入的是1')