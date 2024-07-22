def sortTuple(tup:tuple):
    return tuple(sorted(tup,key=lambda i:i[1]))

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

print(sortTuple(tuple1))