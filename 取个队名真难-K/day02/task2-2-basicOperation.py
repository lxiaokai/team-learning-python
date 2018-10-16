#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:34 AM
# @Author  : liangk
# @Site    : 基础运算
# @File    : basicOperation.py
# @Software: PyCharm


class BasicOperation(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if (self.num2 == 0):
            return -1
        return self.num1 / self.num2


# 程序主入口
if __name__ == '__main__':

    print("Welcome To Use DaBiaoGuo’s The calculator")
    print("****************************")
    print("***** 1.add      2.sub *****")
    print("***** 3.mul      4.div *****")
    print("******     0.exit      *****")
    print("****************************")

    while True:
        inputNum = input("\nPlease select a menu:")
        if int(inputNum) > 0 and int(inputNum) <= 4:

            print("please input num1:")
            num1 = int(input())
            print("please input num2:")
            num2 = int(input())
            result = -1

            if int(inputNum) == 1:
                result = BasicOperation(num1, num2).addition()

            elif int(inputNum) == 2:
                result = BasicOperation(num1, num2).subtraction()

            elif int(inputNum) == 3:
                result = BasicOperation(num1, num2).multiplication()

            elif int(inputNum) == 4:
                result = BasicOperation(num1, num2).division()

            if result == -1:
                print("Divisor cannot be zero, please try again~")
            else:
                print("The result is %f" % result)
        elif int(inputNum) == 0:
            exit("Next Time You Use")
        else:
            print("The wrong choice，Please try again")
