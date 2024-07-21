def countListOccurrences(arr:list):
    obj = dict()
    for item in arr:
        if obj.get(item):
            obj[item]+=1
        else:
            obj[item]=1
    return obj

print(countListOccurrences([11, 45, 8, 11, 23, 45, 23, 45, 89]))