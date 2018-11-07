# -*- coding: utf-8 -*-
import os
from multiprocessing import Process
# 子程序要执行的代码
def run_proc(name):
    print('run child process %s (%s)' % (name,os.getpid()))
if __name__ =="__main__":
    # Linux/Unix操作系统提供一个fork()系统调用，调用一次，返回两次
    # 因为操作系统自动把当前进程（父进程）复制了一份（子进程），分别在父进程和子进程内返回
    # 子进程永远返回 0 ，父进程返回子进程的ID
    # 一个父进程可以fork出很多子进程，所以父进程要记下每个进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID
    # Python的 os 模块封装了常见的系统调用
    print('Process(%s) start...' % os.getpid())  
    pid = os.fork()
    if pid == 0:
        print('我是子进程%s，我的父进程是 %s' %(os.getpid(),os.getppid()))
    else:
        print('我%s 仅创建了一个子进程 %s' % (os.getpid(),pid))
    # multprocessing 模块跨平台版本的多进程模块
    # 提供一个process类来代表一个进程对象

    print('Parent peocess %s ' % os.getpid())
    p = Process(target = run_proc,args = ('test',))
    print('child process will start')
    p.start()
    p.join()
    print('Child process end')

    # Pool 