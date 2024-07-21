def removeListKeys(dic:dict,keys:list):
    for key in keys:
        dic.pop(key)
    return dic

sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}

keys = ["name", "salary"]

print(removeListKeys(sample_dict,keys))