# @time 2018/10/22 15:10
# @Author lhf
from itertools import count
show_list = []
def show(func):
    def interesting_function(num):
        if len(show_list) == 0:
            for a in range(0, num):
                show_list.append(a)
        print("输出：")
        return print(func(num))
    return interesting_function
@show
def isPrime(n):
    if n <= 1:
        return str(n) + "不是素数"
    for i in count(2):
        if i * i > n:
            return str(n) + "是素数"
        if n % i == 0:
            return str(n) + "不是素数"
def out():
    for a in show_list:
        isPrime(a)
if __name__ == '__main__':
    print("第1次遍历list")
    out()
    isPrime(10)
    print("第2次遍历list")
    out()
