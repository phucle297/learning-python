def currAndPrevNumAndSum(n):
    sum = 0
    prev = 0
    for i in range(n):
        sum = prev+i
        print("Current Number:",i,"; Previous Number:",prev,"; Sum:",sum)
        prev = i

currAndPrevNumAndSum(10)