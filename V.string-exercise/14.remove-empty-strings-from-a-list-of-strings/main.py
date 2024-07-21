def removeEmptyStrInList(listStr:list[str]):
    return list(filter(lambda x: x!= '',listStr))

print(removeEmptyStrInList(["Emma", "Jon", "", "Kelly", None, "Eric", ""]))