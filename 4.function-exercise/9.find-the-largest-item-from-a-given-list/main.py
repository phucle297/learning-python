def findMaxItem(list:list):
    max = list[0]
    for e in list:
        if e>max: max=e
    print(max)
    return max

findMaxItem([4, 6, 8, 24, 12, 2])