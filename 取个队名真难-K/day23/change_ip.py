#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 4:31 PM
# @Author  : liangk
# @Site    : 
# @File    : change_ip.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import threading
import requests

# 设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
import socket

socket.setdefaulttimeout(3)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}


class Change_IP:
    def __init__(self):
        pass

    def get_ip(self):
        # 获取代理IP，返回列表
        httpResult = []
        httpsResult = []
        try:
            for page in range(1, 2):
                IPurl = 'http://www.xicidaili.com/nn/%s' % page
                rIP = requests.get(IPurl, headers=headers)
                IPContent = rIP.text
                print
                IPContent
                soupIP = BeautifulSoup(IPContent, 'lxml')
                trs = soupIP.find_all('tr')
                for tr in trs[1:]:
                    tds = tr.find_all('td')
                    ip = tds[1].text.strip()
                    port = tds[2].text.strip()
                    protocol = tds[5].text.strip()
                    if protocol == 'HTTP':
                        httpResult.append('http://' + ip + ':' + port)
                    elif protocol == 'HTTPS':
                        httpsResult.append('https://' + ip + ':' + port)
        except:
            pass
        return httpResult, httpsResult

    # 验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页 http
    def cip(self, x, y):
        f = open("ip_http.txt", "a")
        f.truncate()
        try:
            print(x + y)
            requests.get('http://ip.chinaz.com/getip.aspx', proxies={'http': x + ":" + y}, timeout=3)
        except:
            print('f')
        else:
            print('---------------------------success')
            f.write(x + ':' + y + '\n')

    # 验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页。https
    def csip(self, x, y):
        f = open("ip_https.txt", "a")
        f.truncate()
        try:
            print(x + y)
            requests.get('https://www.lagou.com/', proxies={'https': x + ":" + y}, timeout=3)
        except:
            print('f')
        else:
            print('---------------------------success')
            f.write(x + ':' + y + '\n')

    def main(self):
        httpResult, httpsResult = self.get_ip()

        threads = []
        open("ip_http.txt", "a").truncate()
        for i in httpResult:
            a = str(i.split(":")[-2][2:].strip())
            b = str(i.split(":")[-1].strip())
            t = threading.Thread(target=self.cip, args=(a, b,))
            threads.append(t)

        for i in range(len(httpResult)):
            threads[i].start()
        for i in range(len(httpResult)):
            threads[i].join()

        threads1 = []
        open("ip_https.txt", "a").truncate()
        for i in httpsResult:
            a = str(i.split(":")[-2][2:].strip())
            b = str(i.split(":")[-1].strip())
            t = threading.Thread(target=self.csip, args=(a, b,))
            threads1.append(t)

        for i in range(len(httpsResult)):
            threads1[i].start()
        for i in range(len(httpsResult)):
            threads1[i].join()

# if __name__ == '__main__':
#     # main()
#     print('获取ip地址完毕~')
#     fp = open('ip_http.txt', 'r')
#     ips = fp.readlines()
#     url = 'https://www.baidu.com'
#     proxy_list = []
#     for ip in ips:
#
#         #     ip = p.strip('\n').split('\t')
#         proxy = 'http:\\\\' + ip
#         # print(proxy)
#         try:
#             s = requests.get(url, params={proxy:proxy})
#             print(s)
#         except Exception as e:
#             print(e)
#     proxies = {'proxy': proxy}
#     proxy_list.append(proxies)
# print(proxy_list)
