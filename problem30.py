import math



sums = []
for i in range (1000, 1000000):
    nums = list(map(int, str(i)))
    temp = 0
    for j in range(0, len(nums)):
        temp += math.pow(nums[j],5)
    if i == temp:
        sums.append(i)

print (sums)

sum_=0
for n in sums:
    sum_ += n
print (sum_)
