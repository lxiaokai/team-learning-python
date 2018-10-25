#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 4:39 PM
# @Author  : liangk
# @Site    : json文件读写
# @File    : task11-1.py
# @Software: PyCharm

import json

# 程序主入口
if __name__ == '__main__':
    test_json = {
        'human': {
            'fatboy': [
                {
                    'name': 'lishao',
                    'age': 25
                },
                {
                    'name': 'shaofeng',
                    'age': 26
                }
            ]
        }
    }

    print('原数据:', test_json)
    json_string = json.dumps(test_json)
    print('json格式化:', json_string)

    new_dict = json.loads(json_string)
    print('转字典:', new_dict)

    print('写文件')
    with open('test_json.json', 'w') as f:
        # 注意这里使用的是dump 而不是dumps
        json.dump(new_dict, f)
        # 注意下面的写入内容
        # json.dump(json_string, f)

    with open('test_json.json', 'r') as f:
        # 注意这里使用的是load 而不是loads
        read_dic = json.load(f)
        print(read_dic)
