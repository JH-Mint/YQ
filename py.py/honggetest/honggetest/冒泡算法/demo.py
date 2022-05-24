mylist = [1, 4, 5, 0, 6]
def bubb(mylist):
    length = len(mylist)
    for i in range(0, length-1):
        for j in range(0, length-1):
            if mylist[j] > mylist[j+1]:
                tmp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = tmp

        for item in mylist:
            print(item)
        print("******************")
bubb(mylist)