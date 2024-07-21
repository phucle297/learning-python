def showElementFrom2List(list1:list, list2:list):
    # return set(zip(list1,list2))
    n = min(len(list1),len(list2))
    newSet = set()
    for i in range(n):
        newSet.add((list1[i],list2[i]))
    return newSet

first_list = [2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9]
second_list = [4, 9, 16, 25, 36, 49, 64]
print(showElementFrom2List(first_list,second_list))