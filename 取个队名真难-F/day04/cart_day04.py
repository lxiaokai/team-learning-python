# @time 2018/10/18 10:38
# @Author lhf
from itertools import count
# #素数曾称质数。一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数
# 运用python的itertools模块
def isPrime1(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False
def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    i = int(input("请输入需要判断的素数:"))
    print(i, "判断是否是素数=", isPrime(i))
    print(i, "使用模块判断是否是素数=", isPrime1(i))
    print("额外输出0~99中的素数集合：")
    list = []
    for i in range(0, 100):
        if isPrime(i):
            list.append(i)
    print(list)
