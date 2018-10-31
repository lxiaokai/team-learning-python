# -*- coding: utf-8 -*-
import requests
if __name__ =="__main__":
    Url = 'https://m10.music.126.net/20181025110650/cf49d099633c1fdd15bf8509386ac0fe/ymusic/e627/765b/7bbd/63198cca3f00a94bb0952dc1f0d507e7.mp3'
    Data = requests.get(Url).content
    with open('my.mp3','wb') as f:
        f.write(Data)