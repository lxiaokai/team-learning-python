# @time 2018/10/25 14:36
# @Author lhf
import os
from urllib import parse

import requests

img_url = 'http://img.shujuren.org/pictures/GB/57ff13a89b3b8.png'
mp4_url = 'http://www.runoob.com/try/demo_source/movie.mp4'
# mp3_url = 'https://m10.music.126.net/20181025110650/cf49d099633c1fdd15bf8509386ac0fe/ymusic/e627/765b/7bbd/63198cca3f00a94bb0952dc1f0d507e7.mp3'
mp3_url = 'https://m10.music.126.net/20181025152541/9325f18b124a092dee12b9f9391f50e2/ymusic/e627/765b/7bbd/63198cca3f00a94bb0952dc1f0d507e7.mp3'


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


def download(url, name, save_path):
    # 名称
    url_data = parse.urlparse(url=url)
    # 请求参数
    url_param = parse.parse_qs(url_data.query)
    # 扩展名
    ext_name = ''
    try:
        ext_name = url_param['f'][0]  # 有可能为空
    except:
        print("error:", url_param);
    # 图片路径
    url_path = url_data.path
    # 图片标识ID
    url_id = os.path.split(url_path)[1]
    # 图片名称
    if name == '':
        save_name = url_id + '.' + ext_name
    else:
        save_name = name
    img_path = os.path.join(save_path, save_name)
    with open(img_path, 'wb') as o:
        data = requests.get(url)
        o.write(data.content)


if __name__ == '__main__':
    makeDir('img')
    download(img_url, '', 'img')
    makeDir('mp4')
    download(mp4_url, '', 'mp4')
    makeDir('mp3')
    download(mp3_url, 'what.mp3', 'mp3')
