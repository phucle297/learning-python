dir = './II.input-and-output-exercise/6.write-all-content-of-a-given-file-into-a-new-file-by-skipping-line-number-5/'
def readAndSkipLine5():
    with open(dir+'input.txt','r') as fp:
        lines = fp.readlines()
    with open(dir+'output.txt','w') as fp:
        counter = 0
        for line in lines:
            if counter==4:
                counter+=1
                continue
            fp.write(line)
            counter+=1
    return
readAndSkipLine5()