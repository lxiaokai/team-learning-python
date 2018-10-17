# @time 2018/10/17 10:41
# @Author lhf

# task02
import math
if __name__ =="__main__":
    try:
        radius = float(input("输入圆得半径:"))
        circumference = 2 * math.pi * radius
        area = math.pi * radius * radius
        print("圆的周长：", circumference)
        print("圆的面积：", area)
    except:
        print("输入有误")