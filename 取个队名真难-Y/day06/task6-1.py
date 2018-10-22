# -*- coding: utf-8 -*-
from collections import Iterable
if __name__ =="__main__":
    # 构造一个1，3，5，7，...，99的列表
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n + 2
    print(L)
    # 切片
    # 取前N个元素
    L = ['Mical','John','linda','lily','hola']
    r = []
    n = 3
    for i in range(n):
        r.append(L[i])
    print(r)
    # 切片操作符
    print(L[0:3]) # 从0取到 3 ，但不包括3，如果第一个索引为0，还可以省略
    # 迭代
    # 定一个list或tuple，可以通过for循环来遍历
    d = {'a':1,'b':2,'c':3}
    for key in d:
        print(key)
    # 默认dict迭代的是key ，若要迭代value 可以用for value in d.value()
    # 字符串也是可迭代对象
    ch = 'abscdcd'
    for c in ch:
        print(c)
    # 如何判断一个对象是可迭代对象，通过collections模块的iterable
    print(isinstance('adb',Iterable))
    print(isinstance([1,2,3],Iterable))
    print(isinstance(123,Iterable))
    # emumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    for i ,value in enumerate(['A','B','C']):
        print(i,value)
    # 列表生成器
    # List Comprehensions
    print(list(range(1,11)))
    # 生成[1x1,2x2,3x3,...10x10]
    L = []
    for x in range(1,11):
        L.append(x*x)
    print(L)
    print([x*x for x in range(1,11)])
    # for循环后面加上if判断，筛选出仅偶数的平方
    print([x*x for x in range(1,11) if x%2==0])
    # 使用两层循环，生成全排列
    print([m+n for m in 'ABC' for n in 'XYZ'])
    # for 循环可以同时使用两个甚至多个变量，比如dict 的item()可以同时迭代key和value
    d = {'x':'A','y':'B','z':'C'}
    for k,v in d.items():
        print(k,'=',v)
    # 列表生成式子也可以使用两个变量生成list
    print([k+ '='+v for k,v in d.items()])
    # 把一个list中的所字符串都变成小写
    L = ['Hello','world','IBM','Apple']
    print([s.lower() for s in L])
    # 生成器
    # 不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
    # 创建一个generator 
    # 方法1：把列表生成式的[]改成()
    L = [x * x for x in range(10)]
    print(L)
    g = (x * x for x in range(10))
    print(g)
    # 打印generator的每一个元素 用next()
    print(next(g))
    # generator也是可迭代元素
    for n in g:
        print(n)
    # 迭代器
    # 可迭代对象：Iterable
    # 使用isinstance()判断一个对象是否是Iterable对象
    # 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

    