# -*- coding: utf-8 -*-
if __name__ =="__main__":
   # try:
    f =open('index.txt','r')
        #print(f.read())
    #finally:
        #if f:
            #f.close()
    # with open('index.txt','r') as f:
       # print(f.read())
    # for line in f.readline():
        # print(line.strip())

    # 二进制文件用rb模式打开
    # f = open('/path/xxx.jpg','rb')
    # f.read()
    # 字符编码
    # 要读取非UTF-8编码的文本文件 需要给open()函数传入encoding参数
    # f = open('index.txt','r',encoding = 'gbk')
    # print(f.read())

    # 写文件
    # w 会覆盖 a 是追加
    f = open('index.txt','a')
    f.write('hello,world')
    f.close()
    f = open('index.txt','r')
    print(f.read())
    