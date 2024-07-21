def identicalItems(set1:set,set2:set):
    return set1.intersection(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(identicalItems(set1,set2))