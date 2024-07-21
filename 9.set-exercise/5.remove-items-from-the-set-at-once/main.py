def removeItemsFromTheSet(data:set,items:list):
    data.difference_update(items)
    return data
set1 = {10, 20, 30, 40, 50}

print(removeItemsFromTheSet(set1,[10,20,30]))