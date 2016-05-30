def number_of_digits(num):
    return len(str(num))

def update_fibonacci(n_1, n_2):
    return n_1 + n_2

def find_fibonnaci_up_to_digit(digit):
    fib_seq = []
    fib_seq.append(1)
    fib_seq.append(1)
    n = len(fib_seq)
    fib_seq.append(update_fibonacci(fib_seq[n-1], fib_seq[n-2]))

    while number_of_digits(fib_seq[-1]) < digit:
        n = len(fib_seq)
        fib_seq.append(update_fibonacci(fib_seq[n-1], fib_seq[n-2]))
    return len(fib_seq)

print find_fibonnaci_up_to_digit(1000)
