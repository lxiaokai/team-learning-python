#/use/bin/python
# -*- coding: utf-8 -*-
#判断语句
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
	
a=int(iput("please input a number:")
if a>=15:
	print("15 is right")
else:
	print("you are wrong!")
	
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
	

#for 循环
for iterating_var in sequence:
   statements(s)

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
	
sum=1
for x in [3,4,5,6,7]:
	sum=sum+x
	print(sum)
	
#while循环语句
while 判断条件：
    语句

n=100
sum=0
while n>0:
	sum=sum+n
	n=n-2
	print("1 到 %d 之和为: %d" % (n,sum))

