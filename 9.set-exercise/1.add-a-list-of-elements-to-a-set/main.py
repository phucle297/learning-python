def addListToSet(setData:set, listData:list):
    setData.update(listData)
    return setData

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

print(addListToSet(sample_set,sample_list))