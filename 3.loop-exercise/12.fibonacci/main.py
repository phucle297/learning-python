def fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    return -1

print(fibonacci(10))

# Dynamic programming

memorize = [0,1]

def dpFibonacci(n):
   if n<= 0:
        print("Incorrect input")
   elif n<=len(memorize):
       return memorize[n-1]
   else:
       res = dpFibonacci(n-1)+dpFibonacci(n-2)
       memorize.append(res)
       return res
   return

print(dpFibonacci(10))