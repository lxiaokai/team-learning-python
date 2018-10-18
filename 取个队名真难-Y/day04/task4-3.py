# -*- coding: utf-8 -*-
if __name__ =="__main__":
    # 字典dict:使用key-value存储
    d = {'mike':95,'john':75,'linda':99}
    print(d['mike'])
    # 把数据放入dict，除了初始化指定外，还可以通过key放入：
    d['Adam'] = 67
    print(d)
    # 一个key只对应一个value，多次对一个key放入value，后面的值会把前面的值冲掉
    # key不存在，会报错
    # 避免key不存在的错误的两种方法：
    # 1.通过in判断key是否存在
    print('Adam' in d)
    # 2.通过get()方法，如果key不存在，可以返回None，或者自己指定的value
    print(d.get('ddd',-1)) # 返回None的时候python的交互环境不显示结果
    # 删除一个key，用pop(key)方法
    # dict内部存放的顺序和key放入的顺序是没有关系的

    # dict.fromkeys(seq[, value]):以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
    seq = ('google','taobao','tencent')
    d = dict.fromkeys(seq)
    print('新字典为',d)
    d = dict.fromkeys(seq,10)
    print('新字典为',d)
    # dict.updata()
    d = {'name': 'yyh','age':7}
    d1 = {'sex': 'female'}
    d.update(d1)
    print(d)

    # set：一组key的集合，但不存储value。由于key不能重复，在set中没有重复的key
    # 创建一个set，需要提供一个list作为输入集合
    s = set([1,2,3])
    print(s)

    # 重复元素在list中自动被过滤
    # 通过add(key)添加元素到set中，可以重复添加，但不会有效果
    s.add(2)
    print(s)
    # 通过remove(key)删除元素
    # set可以看做数学意义上的无序和无重复元素的集合，两个set可以做数学意义上的交集并集
    s1 = set([1,2,3])
    s2 = set([2,3,4,5])
    print(s1 & s2)
    print(s1 | s2)