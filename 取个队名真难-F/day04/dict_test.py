# @time 2018/10/18 17:49
# @Author lhf

if __name__ == "__main__":
    dict = {'num1': 1, 'num2': 2, "num3": 3}
    print("输出：dict[num2]=", dict['num2'])
    dict["num2"] = 666
    print("输出：dict[num2]=", dict['num2'])

    del dict['num2']
    print(dict)
    dict["num4"] = 44

    print(dict)

    dict.clear()
    print(dict)

    setList = set(("abc", "edf", "hij"))
    print(setList)

    setList.add("aaadddd")
    setList.add("aaadddd")
    setList.add("aaadddd")
    setList.add("aaadddd")
    print(setList)
