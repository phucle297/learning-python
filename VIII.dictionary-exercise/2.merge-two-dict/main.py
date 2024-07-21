def merge2Dict(dict1:dict, dict2:dict):
    return {**dict1,**dict2}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

print(merge2Dict(dict1,dict2))