# @time 2018/10/25 17:38
# @Author lhf
from openpyxl import Workbook
import requests
URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=&device_id=&token=&src=web&before&limit=10'

if __name__ == '__main__':
    wb = Workbook()
    filename = 'excel练习.xlsx'
    ws1 = wb.active
    ws1.title = "肥？"

    dic = requests.get(URL).json() # 获取掘金十条数据
    lis = dic['d']['list']
    print(lis)

    name = ['名字']
    content = ['内容']
    for i in lis:
        name.append(i['user']['username'])
        content.append(i['content'])

    for (i, m) in zip(name, content):
        col_A = 'A%s' % (name.index(i) + 1)
        col_B = 'B%s' % (name.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = m
    wb.save(filename=filename)
