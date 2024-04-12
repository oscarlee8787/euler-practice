'''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
'''

def is_prime(n):
    if n == 2 or n == 1:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True

def prime_factors(n):
    f = []
    if is_prime(n) is True:
        return set()
    for i in range(2, n, 1):
        if is_prime(i) is True:
            if n%i == 0:
                while n%i == 0:
                    n = int(n/i)
                f.append(i)
            else:
                continue
            if n == 1:
                return set(f)

def funk(n):
    i = 10000
    while i < n:
        # if is_prime(i) is False:
        if len(prime_factors(i)) == 4:
            if len(prime_factors(i+1)) == 4:
                if len(prime_factors(i+2)) == 4:
                    if len(prime_factors(i+3)) == 4: # and prime_factors(i) & prime_factors(i+1) & prime_factors(i+2) & prime_factors(i+3) == set():
                        return i
                    i += 1
                i += 1
            i += 1
        i += 1
        # else:
        #     i += 1


# print(funk(20000))

print(prime_factors(20233))ffffdffcuuyjhv,ncc
