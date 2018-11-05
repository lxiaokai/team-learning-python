#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 3:01 PM
# @Author  : liangk
# @Site    : 
# @File    : download_img.py
# @Software: PyCharm

import os
from urllib import parse
import requests


class Download_image:

    def __init__(self):
        pass

    def makeDir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def download(self, url, name, save_path):
        # 名称
        url_data = parse.urlparse(url=url)
        # 请求参数
        url_param = parse.parse_qs(url_data.query)
        parseResult_path = url_data.path
        if url_param:
            url = url_param['src'][0]
            # 扩展名
            ext_name = url.split('.')[-1]
        else:
            # 扩展名
            ext_name = parseResult_path.split('.')[-1]

        save_name = name + '.' + ext_name
        img_path = os.path.join(save_path, save_name)
        with open(img_path, 'wb') as o:
            data = requests.get(url)
            o.write(data.content)
        print('图片下载完毕-%s' % os.path.abspath(img_path))
