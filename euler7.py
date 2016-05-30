primeNum = 1
prime = 2
i = prime
num = 10001


while primeNum < num:
    for j in range(2,prime+1):
        if(i % j == 0):
            break
        if(j == prime):
            prime = i
            primeNum += 1
    i += 1


print "Prime: %d, PrimeNum: %d\n" % (prime, primeNum)
