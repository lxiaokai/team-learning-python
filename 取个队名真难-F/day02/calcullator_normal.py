# @time 2018/10/16 14:44
# @Author lhf

def add(x, y):
    # 相加

    return x + y


def subtract(x, y):
    # 相减

    return x - y


def multiply(x, y):
    # 相乘

    return x * y


def divide(x, y):
    #相除

    return x / y
def main():
    print("计算两个数字的值:")
    try:
        num1 = int(input("输入第一个数字: "))
        num2 = int(input("输入第二个数字: "))
        print("数字1=" + str(num1) + "和数字2=" + str(num2) + "要做什么操作")
        choice = input("输入1相加，输入2相减，输入3相乘，输入4相除：")
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("肥仔别闹")
    except:
        print("肥仔别闹")

if __name__=="__main__":
    main()