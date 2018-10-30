# @time 2018/10/30 16:10
# @Author lhf
import base64
from datetime import datetime
import time

def bmp_info(data):
    return {
        'width': 200,
        'height': 100,
        'color': 24
    }
if __name__ == '__main__':
    print(time.asctime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # time时间

    # 获取当前时间戳
    print(datetime.now().timestamp())

    print(datetime.now())

    # 时间戳转str日期
    t = 1540891034.595177
    print(datetime.fromtimestamp(t))

    # base64

    s = '肥仔'
    s = base64.b64encode(s.encode('utf-8'))  # 加码
    print(s)

    s = base64.b64decode(s) # 解码
    print(str(s, 'utf-8'))


