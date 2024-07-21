def removeEmptyStrInList(arr:list):
    return list(filter(lambda i:i!='',arr))

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(removeEmptyStrInList(list1))