# -*- coding: utf-8 -*-
# 判断是不是素数
def isPrime(nums,dictonary):
    for num in nums:
        if num > 1:
            for i in range(2,num):
                if (num % i)== 0:
                    break
            else:
                dictonary[str(num)] = '素数'
    return dictonary
    
if __name__ =="__main__":
    dictionary = {}
    nums = [1,2,3,4,5,6,7,8,9,11,13]

    print(isPrime(nums,dictionary))

