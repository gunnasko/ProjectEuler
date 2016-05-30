import numpy

b = []
for i in range (0,1000):
    if((i%3 == 0) or (i%5 == 0)):
        b.append(i)


print "Sum: %d" % sum(b)
print str(b)[1:-1]
