import re
def isNumeric(str):
    pattern = re.compile("^([0-9]+(\.[0-9]+)?)$")
    return pattern.match(str)

def calcMultiply():
    a=input('num1: ')
    while not isNumeric(a):
        a=input("please enter a number! num1: ")
    b=input('num2: ')
    while not isNumeric(b):
        b=input("please enter a number! num2: ")
    a=float(a)
    b=float(b)
    print(a*b)
    return a*b

calcMultiply()