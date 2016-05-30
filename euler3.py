
num = 600851475143 
factors = []
i = 2
while i <= num:
    div = float(num)/i
    if (div).is_integer():
        num = div
        factors.append(i)
    i += 1


print str(factors)[1:-1]
