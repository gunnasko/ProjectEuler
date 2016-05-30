num = 20
lowestValueFound = False
i = 1
while lowestValueFound == False:
    for j in range(1,num+1):
        if (i%j) != 0:
            break
        if j == num:
            lowestValueFound = True
            print "Found value %d\n" % i
    i += 1
