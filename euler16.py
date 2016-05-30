import math

num_big = math.pow(2,1000)
print num_big
num = long(num_big)
temp_string = str(num)
print temp_string
sum_num = 0
for c in temp_string:
    print c
    sum_num = sum_num + int(c)

print sum_num
