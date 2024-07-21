def replace20With200(arr:list):
    return list(map(lambda i: i if i!=20 else 200,arr))

list1 = [5, 10, 15, 20, 25, 50, 20]

print(replace20With200(list1))