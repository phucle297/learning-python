def formatStr(a,b,c):
    sentence = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
    print(sentence.format(a,b,c))
    return

formatStr(33, 1500, 45.45)
