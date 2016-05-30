def get_decimals_as_str(num):
    return "{:.3000f}".format(num).split(".")[-1]

#print 1/73.
print get_decimals_as_str(1/983.)

def get_pattern(num_str):
    i = 0
    #print "num_str: " + num_str
    pattern_len = 1
    c_slice = num_str[0:1]
    longest_pattern = c_slice
    for i in range(0, len(num_str)):
        c_slice = num_str[0:i+1]
        #print "c-slice: " + c_slice
        #print "num_str: " + num_str[i+1:(i+1) + len(c_slice)

        if len(c_slice)*2 > len(num_str):
            return longest_pattern

        if len(c_slice) > 1:
            if c_slice[i] == c_slice[i-1] and c_slice[i] != '0':
                return longest_pattern

        if(c_slice == num_str[i+1:(i+1) + len(c_slice)] and c_slice != '0'):
            #print "found pattern!"
            return c_slice

def find_longest_pattern(d):
    patterns = []
    for i in range(1,d):
        patterns.append(get_pattern(get_decimals_as_str(1./i)))
    print patterns
    pattern_lengths = map(len, patterns)
    return pattern_lengths.index(max(pattern_lengths)) + 1

print(find_longest_pattern(1000))
