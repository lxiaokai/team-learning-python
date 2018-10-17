# -*- coding: utf-8 -*-
if __name__ =="__main__":
    # ord()函数获取字符串的整数表示，chr()函数把编码转换为对应的字符
    print(ord('A'))
    print(ord('中'))
    print(chr(66))
    print(chr(23432))
    # 如果知道字符的整数编码，还可以用十六进制写str
    print('\u4e2d\u6587')
    # python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干字节
    # 如果要在网络上传输，或者保存到磁盘上，需要把str变为以字节为单位的bytes
    # python 对bytes类型的数据用带 b 前缀的单引号或双引号表示
    x = b'ABC' # bytes的每个字符只占一个字节
    # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    # 纯英文的str可以用ASCII码编码为bytes,内容是一样的
    # 含有中文的str可以用utf-8编码为bytes
    # 含有中文的str无法用ASCII编码，因为中文编码超过了ASCII编码的范围
    print('ABC'.encode('ascii'))
    print('中文'.encode('utf-8'))
    # 我们从网络或者磁盘上读取了字节流，读到的数据就是bytes 
    # 要把bytes 变为str ，需要用decode()方法
    print(b'ABC'.decode('ascii'))
    # 如果bytes中有一小部分无效的字节，可以传入error='ignore'忽略错误的字节
    print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
    # 计算str中包含多少个字符 用len()函数
    print(len('ABC'))
    print(len('中文'))
    # 如果换成bytes len()函数计算字节数
    print(len(b'ABC'))
    print(len('中文'.encode('utf-8')))
    # 格式化输出
    # 采用的格式化方式 用%实现
    # %s表示用字符串替换，%d表示用整数替换
    # 有几个%?占位符，后面就跟几个变量或值
    # 如果只有一个%?，括号可以省略
    a = 'world'
    print('hello %s' % a)
    print('hi,%s,you have $%d'%('yyh',1000))
    print('%2d-%02d'%(3,1))
    print('%.2f'%3.1415926)
    # 如果不确定应该用什么 %s永远起作用，会把任何数据类型转换为字符串
    # %% 表示一个 %
    
    # format():用传入的参数依次替换占位符{0}、{1}、{2}...
    print('hello,{0},成绩提示了{1:.1f}%'.format('小米',17.125))

    #########################
    # list 和 tuple

    # list:有序集合，可随意添加和删除其中的元素
    classmates = ['yyh','sw','ly']
    print(classmates)
    # 用len()可以获得list元素的个数
    print(len(classmates))
    # 用索引访问list中每个元素的位置，从0开始
    # 超出时，会报 IndexError的错误
    # 取最后一个元素时，除了计算索引位置，还可以用-1做索引
    print(classmates[-1])
    # 以此类推，可以取倒数第2 倒数第3个
    print(classmates[-2])

    # 可以往list中追加元素到末尾
    classmates.append('pmy')
    print(classmates)

    # 把元素插到指定的位置
    classmates.insert(1,'fze')
    print(classmates)

    # 删除 用pop(),从末尾删除
    print(classmates.pop())
    print(classmates)
    
    # 删除指定位置用pop(i)

    # 要把某个元素替换成别的元素，直接赋值给对应的索引位置
    classmates[1]='jack'

    # list里面的元素数据类型可以不同
    l = [123,'apple',True]

    # list 元素也可以是另一个list
    s = [123,['python',321],'hhh']
    print(len(s))

    # tuple: 和list类似，但是一旦初始化就不能修改
    classmates1 = ['mike','john','tracy']
    # 没有append()和insert()一类的方法，但是仍然可以获取元素
    # tuple不可变，所以代码更安全
    # 定义一个空的tuple
    t = ()
    # 定义只有一个元素的tuple,必须加逗号
    t = (1,)

    # 可变的tuple
    t = ('a','b',['A','B']) # 第三个元素是一个list
    print(t)
    t[2][0] = 'X'
    print(t)