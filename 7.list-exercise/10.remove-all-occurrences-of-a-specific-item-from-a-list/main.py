def removeAllSpecificValue(arr:list,num:int):
    return list(filter(lambda item:item !=num,arr))

list1 = [5, 20, 15, 20, 25, 50, 20]

print(removeAllSpecificValue(list1,20))
