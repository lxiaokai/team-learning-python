# -*- coding: utf-8 -*-
import json
from pprint import pprint
from collections import OrderedDict
if __name__ =="__main__":
    data = {
        'name': 'yyh',
        'age':18,
        'heigh':168,
        'addr':'beijing'
    }
    # 字符串处理json.dumps() json.loads()
    # json_str = json.dumps(data)
    # print(json_str)
    # data = json.load(json_str)

    # 文件处理 json.dump() json.load()
    # writing JSON data
    with open('data.json','w') as f:
        json.dump(data,f)
     
    # Reading data back
    with open('data.json','r') as f:
        data = json.load(f)
    print(data)
    # pprint 按照key的字母顺序打印
    pprint(data)

    # JSON解码会根据提供的数据创建dict 或 lists 
    # 如果想要创建其他类型的对象，可以给json.load()传递object_pairs_hook 或object_hook参数

    s = '{"name":"hhh","shares": 50,"price": 490.1}'
    data1 = json.loads(s,object_pairs_hook=OrderedDict)
    data2 = json.loads(s)
    print(data1)
    print(data2)
    # 将一个JSON字典转换为一个python对象例子
    class JSONObject:
        def __init__(self,d): # __init__是python中的构造函数
            self.__dict__ = d

    data = json.loads(s,object_hook=JSONObject)
    print(data.name)

    # 编码JSON的时候，想获得漂亮的格式化字符串，可以使用json.dumps()的indent参数
    print(json.dumps(s,indent = 4))