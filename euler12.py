import math
divisorsLen = 0
divisorsToCheck = 500
lastTriangleNum = 1
triangleNumLength = 1


while(divisorsLen <= divisorsToCheck):
    divisorsLen = 0 #Reset list
    newTriangleNum = lastTriangleNum + triangleNumLength + 1
    triangleNumLength = triangleNumLength + 1
    lastTriangleNum = newTriangleNum
    for i in range (1, int(math.sqrt(newTriangleNum))+1):
        if newTriangleNum % i == 0:
            if i != newTriangleNum/i:
                divisorsLen = divisorsLen + 2
            else:
                divisorsLen = divisorsLen + 1

print str(divisorsLen) + " - " +  str(newTriangleNum)
