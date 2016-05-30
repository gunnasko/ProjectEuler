class Type:
    Perfect, Deficient, Abundant = range(3)


def get_proper_divisors(n):
    ret = []
    for i in range(1, n-1):
        if n%i == 0:
            ret.append(i)
    return ret

def get_num_type(num):
    sum_num = sum(get_proper_divisors(num))
    if sum_num == num:
        return Type.Perfect
    elif sum_num < num:
        return Type.Deficient
    else:
        return Type.Abundant

def sum_num(a,b):
    return

def get_all_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(1, limit):
        if get_num_type(i) == Type.Abundant:
            abundant_numbers.append(i)
    return abundant_numbers

print get_all_abundant_numbers(60)
def get_sum_of_all_two_abundant_numbers(limit):
    numbers = get_all_abundant_numbers(limit)
    is_sum_of_abundent = [0]*(limit + 1)
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            new_sum = numbers[i] + numbers[j]
            if(new_sum <= limit):
                is_sum_of_abundent[new_sum] = 1
            else:
                break
    return is_sum_of_abundent

def get_sum_of_items_not_in_list(limit):
    numbers = get_sum_of_all_two_abundant_numbers(limit)
    total = len(numbers)
    sum_num = 0
    for i in range(0, total):
        if(numbers[i] == 0):
            sum_num = sum_num + i
    return sum_num

print get_sum_of_items_not_in_list(28123)
