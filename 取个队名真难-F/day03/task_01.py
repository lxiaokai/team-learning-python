# @time 2018/10/17 10:52
# @Author lhf

# task01
if __name__ == "__main__":
    try:
        print("输入两个要计算的数字：")
        num1=int(input("输入第一个数字："))
        num2=int(input("输入第二个数字："))
        print("相加=",num1+num2,",相减=",num1-num2,",相乘=",num1*num2,",相除=",num1/num2)
    except:
        print("输入有误")