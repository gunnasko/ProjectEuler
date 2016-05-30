def rule(n):
    ret = 0
    if(n % 2 == 0):
        ret = n/2
    else:
        ret = 3*n + 1
    return ret

startNum = 13
numberOfTries = 1000000
lastNumber = 0
maxChainLength = 0
bestStartNum = 0
for i in range(startNum,numberOfTries):
    chainLength = 0
    lastNumber = i
    while(lastNumber != 1):
        lastNumber = (rule(lastNumber))
        chainLength = chainLength+1

    if maxChainLength < chainLength:
        maxChainLength = chainLength
        bestStartNum = i

print str(bestStartNum) + " - " + str(maxChainLength)
