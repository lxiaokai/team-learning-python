# @time 2018/10/29 13:54
# @Author lhf
import re

# 编写一个简单的正则表达式，验证输入的手机号码是否正确（1开头的11位数字）
# 编写一个简单的正则表达式，验证输入的身份证号码是否正确（18位数字，有的可能最后一个数位为小写x或者大写X）

if __name__ == '__main__':
    while True:
        a = input("输入1判断是否电话号码，输入2判断是否身份证号码：")
        if a == '1':
            num = input('输入需要判断的电话号码：')
            result = re.match(r'^1\d{10}', num)
            print(",len=", len(num))
            if result:
                print("是个电话号码")
            else:
                print("what's this?")
            if num == 'q':
                quit()
        elif a == '2':
            num = input("输入需要判断的身份证号：")
            result = re.match(r"\d{17}[0-9xX]", num)
            print(",len=", len(num))
            if result:
                print("是个身份证")
            else:
                print("what's this?")
            if num == 'q':
                quit()
        elif a == 'q':
            quit()

