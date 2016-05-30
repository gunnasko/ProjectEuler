def evenly_div_numbers (n):
    ret = []
    for i in range(1, n-1):
        if n%i == 0:
            ret.append(i)
    return ret

def d(n):
    return sum(evenly_div_numbers(n))

def get_sum_of_amicable(n):
    sum_num = 0
    start_num = 2
    known_amicables = []
    for i in range(start_num, n ,2):
        if i not in known_amicables:
            j = d(i)
            if (d(j) == i and i != j):
                known_amicables.append(i)
                known_amicables.append(j)
    return sum(known_amicables)

print get_sum_of_amicable(10000)
