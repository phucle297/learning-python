def checkIfValueInDict(dic:dict, value: int):
    if value in dic.values(): return True
    return False

sample_dict = {'a': 100, 'b': 200, 'c': 300}

print(checkIfValueInDict(sample_dict,200))