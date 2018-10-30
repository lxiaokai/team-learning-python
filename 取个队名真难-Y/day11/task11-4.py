# -*- coding: utf-8 -*-
import requests
if __name__ =="__main__":
    videoUrl = 'http://www.runoob.com/try/demo_source/movie.mp4'
    videoData = requests.get(videoUrl).content
    with open('video.mp4','wb') as video:
        video.write(videoData)