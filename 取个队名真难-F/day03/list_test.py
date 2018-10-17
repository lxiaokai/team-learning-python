# @time 2018/10/17 16:51
# @Author lhf

if __name__ =="__main__":

    list=[]
    print("1. list=",list)
    for i in range(0,10):
        list.append(i)
    print("2. list=", list)

    print('list[3]=',list[3])

    for i in range(0,len(list)):
            list[i]=i+90

    print("3.list=",list)

    print("98 index=",list.index(98))

    list.insert(8,77)
    print("4. list=",list)

    list.remove(list[8])

    print("5. list=",list)

    list.reverse()

    print("6. list=",list)

    print("max=",max(list),",min=",min(list))

    list.clear()

    print("7. list=",list)