import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

print( is_prime(4))

maxN = 0
maxAnsProd = 0
for a in range(-1000, 1000):
    for b in range(0, 1000):
        if( is_prime(b)):
            test_prime = True
            n = 0
            while test_prime:

                ans = n*n + a*n + b
                if( ans < 0):
                    test_prime = False
                elif (is_prime(ans)):
                    n += 1
                else:
                    test_prime = False
            if n > maxN:
                maxN = n
                maxAnsProd = a*b

print (maxN)
print (maxAnsProd)
