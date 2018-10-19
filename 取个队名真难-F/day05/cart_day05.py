# @time 2018/10/19 11:31
# @Author lhf
from itertools import count


def isPrime(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False


if __name__ == "__main__":
    i = int(input("请输入需要判断的素数:"))
    print(i, "判断是否是素数=", isPrime(i))
    print("额外输出0~99中的素数字典：")
    list = range(0, 100)
    dict = {}
    a = 0
    for i in list:
        if isPrime(i):
            a += 1
            keyStr = '第' + str(a) + '个'
            dict[keyStr] = i
    print(dict)
