# @time 2018/10/22 15:10
# @Author lhf
import functools
from itertools import count

show_list = []
def show(func):
    def wrapper(num):
        if len(show_list) == 0:
            for i in range(0, num):
                show_list.append(i)
        print("输出：")
        return print(func(num))
    return wrapper
@show
def isPrime(n):
    if n <= 1:
        return str(n) + "不是素数"
    for i in count(2):
        if i * i > n:
            return str(n) + "是素数"
        if n % i == 0:
            return str(n) + "不是素数"
if __name__ == '__main__':
    isPrime(10)
    for i in show_list:
        isPrime(i)
