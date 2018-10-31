# @time 2018/10/31 17:18
# @Author lhf
import os
from urllib import parse
import requests


class MyDownload:

    def __init__(self):
        pass

    def makeDir(self,s):
        if not os.path.exists(s):
            os.makedirs(s)

    def download(self,url, name, save_path):
        # 名称
        url_data = parse.urlparse(url=url)
        # 请求参数
        url_param = parse.parse_qs(url_data.query)

        url = url_param['src'][0]
        # 扩展名
        ext_name =url.split('.')[-1]

        save_name = name + '.' + ext_name
        img_path = os.path.join(save_path, save_name)
        with open(img_path, 'wb') as o:
            data = requests.get(url)
            o.write(data.content)