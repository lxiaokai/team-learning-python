# -*- coding: utf-8 -*-
import math
from functools import reduce
if __name__ =="__main__":
# 函数式编程
# 函数式编程的特点是，允许把函数作为参数传入一个函数，还允许返回一个函数
# 高阶函数
# 变量也可以指向函数
    f = abs
    print(f(-10))
# 函数名也是变量
# 传入函数
# 一个函数可以传入可以接收另一个函数作为参数，这种函数称之为高阶函数
def add(x,y,f):
    return f(x) + f(y)

print(add(-5,6,abs))
# map/reduce
# map()接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6])
print(list(r))
# 把list所有数字转为字符串
print(list(map(str,[1,2,3,4,5])))
# reduce
# reduce把一个函数作用在一个序列[x1,x2,x3,...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
    return x + y
print(reduce(add,[1,3,5,7,9]))
# 把序列【1,3,5,7,9】变换成整数13579
def fn(x, y):
    return x* 10+y
print(reduce(fn,[1,3,5,7,9]))
# filter
# 把传入的函数依次作用于每个元素，然后返回值True还是False决定保留还是丢弃该元素
# 返回Iterator
def is_odd(n):
    return n % 2 ==1
print(list(filter(is_odd,[1,2,3,4,5,6])))
# sorted
# sorted()，接收一个key函数来实现自定义的排序
print(sorted([36,5,-12,9,-21],key = abs))
# 函数作为返回值
# 如果不需要立刻求和，而是在后面的代码中，需要再计算，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print(f())
# 匿名函数
# 装饰器