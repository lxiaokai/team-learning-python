#/usr/bin/python
#-*-coding:utf-8-*-
#函数定义def依次写出函数名、括号、括号中的参数和冒号:在缩进块中编写函数体，函数的返回值用return语句返回。
def my_ab(x):
	if x>=0:
		return x
	else:
		return -x
		
#输入调用
my_ab(-1)

#函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）
#导入上述定义函数后再调用
from abstest import my_ab
my_ab(-9)


#定义一个空函数
def nop()
	pass
	
#求一个二次元方程的解
import math
def quadratic(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        return x1,x2
    elif d==0:
        x=-b/(2*a)
        return x
    else:
        return '此方程无解'

print(quadratic(2,8,1))

#先定义一个函数，传入一个list，添加一个END再返回：定义默认参数要牢记一点：默认参数必须指向不变对象！
#*nums表示把nums这个list的所有元素作为可变参数传进去
#回顾list运用
list1=[1,2,3,4,5,6,7]
list2=['a','b','c','d','e','f','g']
#列表索引从0开始。列表可以进行截取、组合等
print('list1[0]',list1[0])
print('list2[1,2]',list2[1:5])
#list.append(obj)在列表末尾添加新的对象
list3=[10,12,13,14,15]
list3.append(16)
print('list3',list3)

#练习打卡将第二课中的程序改写成函数的形式。
#任意编写一个 List 作为函数的参数，
#判断 List 中的每个元素是否为素数。
#并将是素数的元素打印为字典。（可以随意设置 key）


#/usr/bin/python
#-*-coding:utf-8-*-
numbers=[]
diction={}
def sushu(num):
    if num>1:
        if num==2:
            numbers.append(num)
        else:
            for i in range(2,num):
                if num%i==0:
                    j=num/i
                    break
            else:
                numbers.append(num)
                diction['素数'] = numbers
                return diction

#主程序入口
if __name__ == '__main__':
    list=[1,2,3,4,5,6,7,8,9,10,11]
    for i in list:
        sushu(i)
        print(numbers)
        print(diction)
		



		
		
