import math
min_ = 2
max_ = 100
nums = set()
for a in range(2, max_+1):
    for b in range(2, max_+1):
        nums.add(math.pow(a, b))

#print (nums)
print (len(nums))
