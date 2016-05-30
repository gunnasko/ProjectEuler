
def permutation(prefix, digits, permutations):
    n = len(digits)
    if n == 0:
        #print "Prefix: " + prefix + "-----" + "Digit: " + digits + "<--- New Permutation"
        permutations.append(prefix)
    else:
        for i in range(0, n):
            permutation(prefix + digits[i], digits[0:i] + digits[i+1::], permutations)
            #print "Prefix: " + prefix + "-----" + "Digit: " + digits + "--After"

def get_sorted_permutations():
    permutations = []
    permutation("", "0123456789", permutations)
    map(int,permutations)
    return sorted(permutations)

sorted_permutations = get_sorted_permutations()

print sorted_permutations[1000000]
print sorted_permutations[1000001]
print sorted_permutations[999999]
