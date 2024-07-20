def evenNumbers(start:int,end:int):
    if start%2!=0: start+=1
    list=[]
    for i in range(start, end,2):
        list.append(i)
    print(list)
    return list

evenNumbers(4,30)
