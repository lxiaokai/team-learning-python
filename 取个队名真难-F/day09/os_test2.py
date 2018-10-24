# @time 2018/10/23 14:55
# @Author lhf
import os

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
    # print("输出当前路径绝对路径：", os.path.realpath('.'))
    print("输出当前绝对路径：", os.getcwd())


def use_walk(path):  # 使用os.walk()直接遍历文件和目录
    for p, dir, file in os.walk(path):
        for f in file:
            print("文件：", os.path.join(p, f))
        for d in dir:
            print("目录：", os.path.join(p, d))


def use_digui(path):
    # os.chdir(path)
    for a in os.listdir(path):
        join_path = os.path.join(path, a);
        if not os.path.isdir(join_path):
            print("文件：", join_path)
        else:
            print("目录：", join_path)
            use_digui(join_path)


if __name__ == '__main__':
    action(first_dir)
    action(second_dir)
    action(three_dir)

    change_dir("..")
    change_dir("..")
    change_dir("..")

    print(os.listdir())
    print('使用os.walk输出')
    use_walk(first_dir)
    print('使用递归输出')
    use_digui(first_dir)
