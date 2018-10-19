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