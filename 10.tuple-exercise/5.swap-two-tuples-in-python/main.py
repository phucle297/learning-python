def swap2Tuple(tup1:tuple,tup2:tuple):
    temp = tup1
    tup1 = tup2
    tup2 = temp
    return tup1,tup2

tuple1 = (11, 22)
tuple2 = (99, 88)
print(swap2Tuple(tuple1,tuple2))