# -*- coding: utf-8 -*-
if __name__ =="__main__":
    # 条件判断
    age = 20
    if age >= 18:
        print('your age is ',age)
        print('adult')
    elif age>=6: # elif 是 else if 的缩写
        print('teenager')
    else:
        print('kid')
    
    # 循环
    # for...in
    names = ['mike','john','lucas']
    for name in names:
        print(name)
    # range()可以生成一个整数序列，再通过list()函数可以转换为list
    print(list(range(5)))
    # 计算1-100的整数和
    sum = 0
    for x in range(101):
        sum = sum+x;
    print(sum)
    # break:提前退出循环
    # continue: 跳过当前的这次循环，直接进入下一次循环
    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0:
            continue
        print(n)
    