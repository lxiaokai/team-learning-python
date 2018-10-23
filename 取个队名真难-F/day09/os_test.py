# @time 2018/10/23 14:55
# @Author lhf
from coverage.files import os

# 一级目录language，二级目录python，三级目录learn；并且每个目录下放置一个index.txt文件
first_dir = 'language'
second_dir = 'python'
three_dir = 'learn'
file_name = 'index.txt'


def my_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def action(d):  # 创建并进入目录
    my_mkdir(d)
    os.chdir(d)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(d)


def change_dir(n):
    os.chdir(n)
    print("输出当前路径绝对路径：", os.path.realpath(os.curdir))

def use_walk_dir(path): #使用os.walk()直接遍历文件和目录
    d = os.walk(path)
    for a in d:
        print(a)

def use_digui(path):
    os.chdir(path)
    print(os.listdir())
    for a in os.listdir():
        if os.path.isdir(a):
            use_digui(a)


if __name__ == '__main__':
    action(first_dir)
    action(second_dir)
    action(three_dir)

    change_dir("..")
    change_dir("..")
    change_dir("..")

    print(os.listdir())
    print('使用os.walk输出')
    use_walk_dir(os.curdir)
    print('使用递归输出')
    use_digui(os.curdir)
