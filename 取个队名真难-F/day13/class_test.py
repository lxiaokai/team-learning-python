# @time 2018/10/29 17:24
# @Author lhf

from class_calculator import MyCalculator

if __name__ == '__main__':
    ca = MyCalculator()
    print("计算两个数字的值:")
    try:
        num1 = int(input("输入第一个数字: "))
        num2 = int(input("输入第二个数字: "))
        print("数字1=" + str(num1) + "和数字2=" + str(num2) + "要做什么操作")
        choice = input("输入1相加，输入2相减，输入3相乘，输入4相除：")
        if choice == '1':
            print(num1, "+", num2, "=", ca.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", ca.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", ca.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", ca.divide(num1, num2))
        else:
            ca.output()
    except:
        ca.output()
