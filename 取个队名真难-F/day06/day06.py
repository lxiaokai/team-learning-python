# by lhf
# 斐波那契数列的定义
# f(0) = 1,f(1) = 1,f(n) = f(n-1) + f(n-2)
def f(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1

if __name__ == '__main__':
    a=int(input('输入一个数字:'))
    print('输出斐波那契数列：')
    print(list(f(a)))
