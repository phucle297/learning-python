def squareItemsInList(arr:list):
    # return list(map(lambda i:i*i,arr))
    return [x * x for x in arr]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(squareItemsInList(numbers))