#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 4:03 PM
# @Author  : liangk
# @Site    :
# @File    : task8-1.py
# @Software: PyCharm

from functools import reduce
import time
import functools


def a(x):
    return x * x


def b(x, y):
    return x + y


def c(x):
    return x % 2 == 1


def d(x):
    def d1():
        return print('x = ', x)

    return d1


def log(func):
    """定义一个装饰器函数"""

    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print(time.strftime("%Y年%m月%d日 %I:%M:%S"))


# 程序主入口
if __name__ == '__main__':
    numberList = [1, 2, 3, 4, 5, 6, 7]
    print('初始列表:', numberList)
    # map()传入的第一个参数是f，即函数对象本身。
    # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    print('1. map函数')
    print(list(map(a, numberList)))

    print('2. reduce函数')
    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
    # 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    print(reduce(b, numberList))

    print('3. filter()函数用于过滤序列。')
    print(list(filter(c, numberList)))

    print('4. sorted()函数就可以对list进行排序')
    '''
    iterable：是可迭代类型;
    cmp：用于比较的函数，比较什么由key决定;
    key：用列表元素的某个属性或函数进行作为关键字，有默认值，迭代集合中的一项;
    reverse：排序规则. reverse = True  降序 或者 reverse = False 升序，有默认值。
    返回值：是一个经过排序的可迭代类型，与iterable一样。
    '''
    print(sorted(numberList))
    print(sorted(numberList, key=a))
    print(sorted(numberList, key=c))
    # 倒序
    print(sorted(numberList, reverse=True))

    print('5. 返回函数')
    f = d(1)
    print(f())

    print('6. 匿名函数')
    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
    # 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
    print(list(map(lambda x: x * 10, numberList)))

    print('7. 装饰器')
    '''
        强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
        这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
        decorator就是一个返回函数的高阶函数
    '''
    print(d.__name__)
    print('开始调用装饰器')
    now()

    print('8. 偏函数')
    print(int('12345'))
    print(int('12345', base=8))

    int2 = functools.partialmethod(int, base=2)
    print(int('1'))
    print(int2('0110'))
