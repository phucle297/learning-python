def removeDuplicatesAndFindMinMax(arr:list):
    newSet = set(arr)
    print('unique items ',newSet)
    print('tuple ',tuple(newSet))
    print('min item ',min(newSet))
    print('max item ',max(newSet))

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
removeDuplicatesAndFindMinMax(sample_list)
