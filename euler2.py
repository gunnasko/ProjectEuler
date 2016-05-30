
n_1 = 1
n_2 = 2
n_3 = n_1 + n_2
even_values = []
even_values.append(2)

while(n_3 < 4000000):
    n_1 = n_2
    n_2 = n_3
    n_3 = n_1+n_2
    print "%d," % n_3
    if(n_3 % 2 == 0):
        even_values.append(n_3)

print "Sum: %d\n" % sum(even_values)
print str(even_values)[1:-1]
