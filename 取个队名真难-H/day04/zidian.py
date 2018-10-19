#/use/bin/python

#字典dic,健是唯一的但值可以不必；
#d={key1:value1,key2:value2,key3:value3,...}
#打印输出
dict={'name':'sally','age':'sevnty','fruit':'banana',}
print("dict['name']:",dict['name'])
#修改
dict['name'] = 'kelly'
print("dict['name']:",dict['name'])
#删除
del dict['name']
print("dict['name']:",dict['name'])
#清除内容
dict.clear()
print("dict['age']:",dict['age'])
#删除整个dict
del dict
print("dict['fruit']:",dict['fruit'])

dict1={'test1':'s11','test2':'s12','test3':'banana',}
#计算多少个len(dict1)
print("dict:",len(dict1))
#输出字典 str(dict1)
print("dict:",str(dict1))
#返回类型type(dict)
print("dict:",type(dict))
#获取参数值
dict.get('hell')
dict.get('herrl',-1)
dict.get('name')

#删除dict.pop（）
dict.pop()

#set集合
a=set([1,2,3,4])
a.add(5)
a.remove(5)

#keys()用法
dict.key()

#遍历
for k in dict:
    print ("dict[%s] =" % k,dict[k])
	
#打印
print (dict.items())
print(dict.values())
#udpate()的等价语句
dict = {"a" : "apple", "b" : "banana"}
print (dict)
dict2 = {"c" : "grape", "d" : "orange"}
dict.update(dict2)
print (dict)

#字典的浅拷贝
dict = {"a" : "apple", "b" : "grape"}
dict2 = {"c" : "orange", "d" : "banana"}
dict2 = dict.copy()
print (dict2)


#dict.fromkeys(seq[, value])
dict={'test1':'s11','test2':'s12','test3':'banana',}
seq=('a','b','c')
dict=dict.fromkeys(seq)
print(str(dict))
dict=dict.fromkeys(seq,11)
print(str(dict))

#判断key是否在字典
print('name' in dict)
print('a' in dict)

#通过对key的遍历，遍历整个dict
 
b = {"name":"sally", "age":24}  
for key in b:  
    print ("key=%s, value=%s" % (key, b[key]))
           
for key in b.keys():  
    print ("key=%s, value=%s" % (key, b[key])) 
      
for key in iter(b):  
    print ("key=%s, value=%s" % (key, b[key]))  
      
for key,item in b.items():  
    print ("key=%s, value=%s" % (key, item))  
 
 
