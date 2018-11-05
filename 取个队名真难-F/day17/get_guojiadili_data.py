# @time 2018/11/5 16:08
# @Author lhf
import os
import requests
from bs4 import BeautifulSoup

url = 'http://www.ngchina.com.cn/magazine'


def get_data(def_url):
    request = requests.get(url=def_url)
    print(request.status_code)
    return request.content


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


def download_img(url, save_path, name):
    ext_name = url.split('.')[-1]
    save_name = name + '.' + ext_name
    img_path = os.path.join(save_path, save_name)
    with open(img_path, 'wb') as o:
        data = requests.get(url)
        o.write(data.content)


if __name__ == '__main__':

    re = get_data(url)
    soup = soup = BeautifulSoup(re, 'lxml')
    div = soup.find_all('div', class_='img_list')

    for d in div:
        # 获取图片
        img = d.find('img', class_='s_img')['src']
        # 获取文字
        img_text = d.find('div', 'img_text')
        a = img_text.find_all('a')

        #建立目录
        makeDir(a[0].text)
        # 下载图片
        download_img(img, a[0].text, a[0].text)
        str_list = ''
        for i in a:
            # # 去掉更多内容文字
            # if i == a[-1]:
            #     break
            str_list = str_list + i.text + '\n'

        #加载更多页面
        to_url=url.replace('/magazine',a[-1]['href'])
        # print(to_url)
        to_re=get_data(to_url)
        to_soup = BeautifulSoup(to_re, 'lxml')
        # text_magazine_text=to_soup.find('div',class_='magazine_text')
        # #杂志文字不为空
        # if text_magazine_text:
        #     p_list=text_magazine_text.find_all('p')
        #     for p in p_list:
        #         str_list=str_list+p.text+'\n'

        big_txt_list = to_soup.find('div', class_='big_txt_list')
        #大字文字不为空
        if big_txt_list:
            big_a=big_txt_list.find_all('a')
            for ba in big_a:
                str_list = str_list + ba.text + '\n'


        # 文字内容添加到文本
        with open(a[0].text + '/' + a[0].text + ".txt", 'w', encoding='utf-8') as f:
            f.write(str_list)

