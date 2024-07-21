# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
# There is also the step value, which can be used with any of the above:

# a[start:stop:step] # start through not past stop, by step
# a[::-1]: reverse

def reverseInt(n):
    reversedStr = str(n)[::-1]
    if reversedStr[-1]=='-':
        reversedStr = '-'+reversedStr[:-1]
    print(int(reversedStr))
    return int(reversedStr)

reverseInt(76542)
reverseInt(-1123)