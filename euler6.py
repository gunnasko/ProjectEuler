numbers = range(1,101)
sum_a = 0;
sum_b = 0;
for i in numbers:
    sum_a += numbers[i-1]*numbers[i-1]
    sum_b += numbers[i-1]

sum_b *= sum_b

diff = sum_b - sum_a

print "%d\n" % diff
