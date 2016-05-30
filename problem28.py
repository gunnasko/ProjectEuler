round = 1

diag_sum = 1
add_base = 1
adder = 1
for n in range(3, 1002, 2):
    add_base = adder
    for i in range(1,5):
        #print (diag_sum)
        adder = (n-1)*i + add_base
        print (adder)
        diag_sum += adder

print ("----")
print (diag_sum)
