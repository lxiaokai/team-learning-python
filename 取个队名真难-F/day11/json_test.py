# @time 2018/10/25 15:32
# @Author lhf
import json


class Person(object):
    def __init__(self):
        self.id = ''
        self.username = ''
        self.age = ''
        self.sex = ''


if __name__ == '__main__':
    dic = {'id': 100, 'username': '小强', 'age': '18', 'sex': '男'}
    j_str = json.dumps(dic)  # dict转成json
    print(type(dic), ':', dic)
    print(type(j_str), ':', j_str)

    d = json.loads(j_str)  # str 转成 dict
    print(type(d), ':', d)

    # model 操作
    person = Person()

    person.__dict__ = json.loads(j_str) # json 转成 model
    print(person.__dict__)
    print(person.username)

    print(json.dumps(person.__dict__))  # model 转成 json

