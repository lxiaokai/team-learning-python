# @time 2018/10/25 17:38
# @Author lhf
from openpyxl import Workbook
from openpyxl.styles import Alignment
import requests
import time
from openpyxl.styles import Font

URL = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=&device_id=&token=&src=web&before&limit=10'

if __name__ == '__main__':
    wb = Workbook()
    filename = 'excel练习.xlsx'
    ws1 = wb.active
    ws1.title = "肥"
    dic = requests.get(URL).json()  # 获取掘金十条数据
    lis = dic['d']['list']
    print(lis)

    # 设置单元格的对齐
    alignment = Alignment(
        horizontal='general',  # 水平：常规
        vertical='bottom',  # 垂直：底部对齐
        text_rotation=0,  # 文本方向：0度
        wrap_text=False,  # 自动换行
        shrink_to_fit=False,  # 缩小字体填充
        indent=0  # 缩进0
    )
    # 调用单元格对齐方式
    ws1['A1'].alignment = alignment

    font1 = Font(name=u'微软雅黑', size=20, strike=True, color='000000', vertAlign='subscript', bold=True, italic=False,
                 underline='none')
    ws1['a1'].font = font1
    ws1['b1'].font = font1

    a = 1
    ws1['A%s' % a] = '名字'
    ws1['B%s' % a] = '内容content'
    for i in lis:
        a += 1
        ws1['A%s' % a] = i['user']['username']
        ws1['B%s' % a] = i['content']

    ws1.cell(row=a + 1, column=1).value = '抓取结束时间' + str(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # A列最后一格写上结束时间

    wb.save(filename=filename)
