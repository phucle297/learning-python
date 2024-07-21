def checkSubSet(set1:set,set2:set):
    if len(set1)!=len(set2):
        if set1.issubset(set2):
            set1={}
            print(set1,set2)
            return True
        if set2.issubset(set1):
            set2={}
            print(set1,set2)
            return True
    else:
        if set1.issubset(set2) and set2.issubset(set1):
            set1={}
            set2={}
            print(set1,set2)
            return True
    return False
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print(checkSubSet(first_set,second_set))
print(checkSubSet(first_set,first_set))
print(checkSubSet(second_set,first_set))