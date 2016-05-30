
palin = []
for i in range(1,1000):
    for j in range(1,1000):
        val = i*j
        string = str(val)
        string_reverse = string[::-1]
        if(string == string_reverse):
            palin.append(val)

print str(palin)[1:-1]
print "%d\n" % max(palin)
