def convertTwoListIntoDict(keys:list, values:list):
    return dict(zip(keys,values))

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(convertTwoListIntoDict(keys,values))
