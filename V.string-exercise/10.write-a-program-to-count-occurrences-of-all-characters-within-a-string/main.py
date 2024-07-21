def countOccurrences(s:str):
    obj = dict()
    for ch in s:
        if obj.get(ch):
            obj[ch]+=1
        else:
            obj[ch]=1
    return obj

print(countOccurrences('Apple'))