def uniqueItemsFrom2Sets(set1:set,set2:set):
    return set1.union(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(uniqueItemsFrom2Sets(set1,set2))