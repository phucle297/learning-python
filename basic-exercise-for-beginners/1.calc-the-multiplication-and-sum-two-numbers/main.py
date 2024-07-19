def calcMulOrSum(a,b):
    res = a * b
    if res <= 1000:
        return res
    return a + b

print(calcMulOrSum(20,30))
print(calcMulOrSum(40,60))