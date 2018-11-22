# @time 2018/11/20 14:53
# @Author lhf
import requests
from bs4 import BeautifulSoup

url = "https://www.ip.cn/"
if __name__ == '__main__':
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    div = soup.find(class_='well').text
    print('代理前: '+div)
    proxies = {
        "http": "http://49.86.181.70:8118",
        "https": "https://119.146.2.234:39960",
    }
    re = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(re.content, 'lxml')
    div = soup.find(class_='well').text
    print('代理后: '+div)
