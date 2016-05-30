
for i in range(2,10):
    cycles = []
    remainder = int(1/i)
    for j in range(1,i):
        remainder *= 10;
        remainder %= i;
        print (remainder)
