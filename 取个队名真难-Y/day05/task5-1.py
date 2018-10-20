# -*- coding: utf-8 -*-
if __name__ =="__main__":
    #定义函数 定义一个函数用def
    def my_abs(x):
        if x > 0:
            return x
        else:
            return -x
    print(my_abs(5))
    # 空函数
    def nop():
        pass # pass 可以作为占位符
    # 参数检查：如果参数个数不对，python解释器会自动检查出来：TypeError
    # 参数类型不对的话，Python解释器无法帮助我们检查
    # 修改my_abs，对参数类型做检查，只允许整数和浮点类型的参数
    # 数据类型检查可以用内置函数isinstance()
    def my_abs1(x):
        if not isinstance(x,(int,float)):
            return TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x
    # 函数返回多个值：python函数返回的仍然是但一值，返回tuple
    # 函数的参数
    # 可变参数：传入的参数个数是可变的
    #举例：计算 a2+b2+c2+... 由于参数不确定，可以把 a,b,c作为一个list或者tuplr传进来
    def calc(numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
    print(calc([1,2,3,4]))
    # 利用可变参数将函数简化，将函数的参数变为可变参数
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
    print(calc(1,2,3,4))
    # 如果已经有一个list和tuple 要调用一个可变参数怎么办
    nums = [1,2,3]
    print(calc(*nums))
    # 关键字参数：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
    # 而关键字参数允许你传入0个或含参数名的参数，这些关键字参数在函数内部自动组装魏一个dict
    def person(name,age,**kw):
        print('name',name,'age',age,'other',kw)
    print(person('Michael',30))
    # 可以传入任意个数的关键字参数
    print(person('Adam',45,gender='M',job = 'engineer'))
    # 要限制关键字参数的名字，用命名关键字参数
    def person(name,age,*,city,job):
        print(name,age,city,job)
    print(person('jack',24,city='beijing',job='engnieer'))
    # 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
    def person(name,age,*args,city,job):
        print(name,age,args,city,job)
    # 命名关键字参数必须传入参数名，没有传入参数名，就会报错
    # 命名关键字参数可以有缺省值
    # 使用命名关键字参数时，如果没有可变参数，就必须加一个*作为特殊分隔符