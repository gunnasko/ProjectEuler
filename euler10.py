import math
num = 2000000
#num = 100

primes = []
primes.append(2)
primes.append(3)
primes.append(5)

i = 7
while primes[-1] < num:
    if(i%2 == 0):
        i +=1
    else:
        maxPrim = int(math.sqrt(i))
        for j in range(1,maxPrim+1):
            if(i % j == 0 and j != 1):
                break
            if(j == maxPrim):
                primes.append(i)
        i += 1


print str(primes)

dsum = sum(primes) - primes[-1]
print "Sum: %d\n" % dsum
