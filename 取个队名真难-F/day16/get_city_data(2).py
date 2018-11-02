# @time 2018/11/1 11:15
# @Author lhf
from datetime import datetime

from bs4 import BeautifulSoup
import os
import requests

url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}


def makeDir(s):
    if not os.path.exists(s):
        os.makedirs(s)


def download_get_soup(url):
    request = requests.get(url=url, headers=headers)
    request.encoding = "utf-8"
    # .read().decode('utf-8', 'ignore')
    if not request.status_code == 200:
        return ''
    soup = BeautifulSoup(request.content, 'lxml')
    return soup


def save_file(save_path, a):
    try:
        # makeDir(save_path + "/" + a[1].text + "(" + a[0].text + ")")  # 有链接建个目录
        a[0]['href']
        makeDir(save_path + "/" + a[-1].text)  # 有链接建个目录
        return a[0]['href']
    except:
        try:
            if a[-1].text == '':
                return '.'
            file_name = save_path + '/' + a[-1].text  # 没有链接随便建个文件
            with open(file_name, 'w') as f:
                pass
        except:
            print("报错save_path=", save_path, "文件=", a)
        return '.'


def down_city_data(soup, path):  # 市
    tr = soup.find_all('tr', class_='citytr')
    numCode = []
    strTr = []
    href = []
    for g in tr:
        a = g.find_all('a')
        numCode.append(a[0].text)
        strTr.append(a[-1].text)

        href.append(save_file(path, a))

    return numCode, strTr, href


def down_data(now_path, strTr, href, now_request_url, class1, class2):
    now_request_url = now_request_url.replace(now_request_url.split('/')[-1], href)
    soup = download_get_soup(now_request_url)
    if soup == '':
        print("请求失败_:" + now_request_url)
        return
    else:
        save_path = now_path + '/' + strTr
        tr = soup.find_all('tr', class_=class1)
        numCode_county = []
        href_county = []
        strTr_county = []
        if not tr:
            tr = soup.find_all('tr', class_=class2)
        for t in tr:
            a = t.find_all('a')
            if not a:  # 没有 a 标签，则在td标签内
                td = t.find_all('td')
                numCode_county.append(td[0].text)
                strTr_county.append(td[-1].text)
                href_county.append(save_file(save_path, td))
            else:
                numCode_county.append(a[0].text)
                strTr_county.append(a[-1].text)
                href_county.append(save_file(save_path, a))
        print(strTr_county)
        return numCode_county, strTr_county, href_county, now_request_url


# def down_county_data(now_path, strTr, href):  # 区
#     now_request_url = url.replace(url.split('/')[-1], href)
#     soup = download_get_soup(now_request_url)
#     if soup == '':
#         print("请求失败_区:" + now_request_url)
#         return
#     else:
#         save_path = now_path + '/' + strTr
#         tr = soup.find_all('tr', class_='countytr')
#         numCode_county = []
#         href_county = []
#         strTr_county = []
#         if not tr:
#             tr = soup.find_all('tr', class_='towntr')  # 东莞和中山是towntr
#         for t in tr:
#             a = t.find_all('a')
#             if not a:  # 没有 a 标签，则在td标签内
#                 td = t.find_all('td')
#                 numCode_county.append(td[0].text)
#                 strTr_county.append(td[-1].text)
#                 href_county.append(save_file(save_path, td))
#             else:
#                 numCode_county.append(a[0].text)
#                 strTr_county.append(a[-1].text)
#                 href_county.append(save_file(save_path, a))
#         print(strTr_county)
#         return numCode_county, strTr_county, href_county, now_request_url
#
#
# def down_town_data(now_path, strTr, href, now_request_url):  # 街道
#     now_request_url = now_request_url.replace(now_request_url.split('/')[-1], href)
#     soup = download_get_soup(now_request_url)
#     if soup == '':
#         print("请求失败_街道:" + now_request_url)
#         return
#     else:
#         save_path = now_path + '/' + strTr
#         tr = soup.find_all('tr', class_='towntr')
#         numCode_town = []
#         strTr_town = []
#         href_town = []
#         if not tr:
#             tr = soup.find_all('tr', class_='villagetr')  # 东莞和中山是villagetr
#         for t in tr:
#             a = t.find_all('a')
#             if not a:  # 没有 a 标签，则在td标签内
#                 td = t.find_all('td')
#                 numCode_town.append(td[0].text)
#                 strTr_town.append(td[-1].text)
#                 href_town.append(save_file(save_path, td))
#             else:
#                 numCode_town.append(a[0].text)
#                 strTr_town.append(a[-1].text)
#                 href_town.append(save_file(save_path, a))
#
#         return numCode_town, strTr_town, href_town, now_request_url
#
#
# def down_village_data(now_path, strTr, href, now_request_url):  # 居委会
#     now_request_url = now_request_url.replace(now_request_url.split('/')[-1], href)
#     soup = download_get_soup(now_request_url)
#     if soup == '':
#         print("请求失败_居委会:" + now_request_url)
#         return
#     else:
#         save_path = now_path + '/' + strTr
#         tr = soup.find_all('tr', class_='villagetr')
#         numCode_village = []
#         strTr_village = []
#         href_village = []
#         # if not tr:
#         #     tr = soup.find_all('tr', class_='towntr')  # 东莞和中山是towntr
#         for t in tr:
#             a = t.find_all('a')
#             if not a:  # 没有 a 标签，则在td标签内
#                 td = t.find_all('td')
#                 numCode_village.append(td[0].text)
#                 strTr_village.append(td[-1].text)
#                 href_village.append(save_file(save_path, td))
#             else:
#                 numCode_village.append(a[0].text)
#                 strTr_village.append(a[-1].text)
#                 href_village.append(save_file(save_path, a))
#
#         return numCode_village, strTr_village, href_village, now_request_url


if __name__ == '__main__':
    # 获取当前时间戳
    start_time = datetime.now().timestamp()
    print('开始时间：', datetime.now())

    soup = download_get_soup(url.replace(url.split('/')[-1], '44.html'))  # 广东省
    if soup == '':
        print("请求失败")
    else:
        now_path = '广东省'
        makeDir(now_path)
        # 获取市
        numCode, strTr, href = down_city_data(soup, now_path)
        for h in href:
            if not h == '.':
                # 获取区
                numCode_county, strTr_county, href_county, now_request_url = down_data(now_path,
                                                                                       strTr[href.index(h)], h, url,
                                                                                       'countytr', 'towntr')
            for hc in href_county:
                if not hc == '.':
                    try:
                        # 获取街道
                        numCode_town, strTr_town, href_town, now_request_url_town = down_data(
                            now_path + '/' + strTr[href.index(h)], strTr_county[href_county.index(hc)], hc,
                            now_request_url, 'towntr', 'villagetr')
                        pass
                        for ht in href_town:
                            if not ht == '.':
                                try:
                                    # 获取居委会
                                    down_data(now_path + '/' + strTr[href.index(h)] + '/' + strTr_county[
                                        href_county.index(hc)], strTr_town[href_town.index(ht)], ht,
                                              now_request_url_town, 'villagetr', '')
                                except Exception as e:
                                    print('解析居委会出错:', e)
                    except Exception as e:
                        print('解析街道出错:', e)

        print("结束时间：", datetime.now())
        end_time = datetime.now().timestamp()
        print('用时：', end_time - start_time)
