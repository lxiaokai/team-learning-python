# @time 2018/10/17 17:22
# @Author lhf

if __name__ == "__main__":

    tup1=(0,1,3)
    print("1.tup1=",tup1)

    print("tup[1]=",tup1[1])

    try:
        tup1[1]=33
    except:
        print("TypeError: 'tuple' object does not support item assignment")

    # del tup; error
    print(tup1)