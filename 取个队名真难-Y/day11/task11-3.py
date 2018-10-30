# -*- coding: utf-8 -*-
import requests
if __name__ =="__main__":
    imgUrl = 'http://img.shujuren.org/pictures/GB/57ff13a89b3b8.png'
    imgData = requests.get(imgUrl).content
    with open('my.jpg','wb') as f:
        f.write(imgData)