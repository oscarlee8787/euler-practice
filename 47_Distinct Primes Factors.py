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

def primes(n):
    i = 2
    s = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            s.add(i)
    if n > 1:
        s.add(n)
    return len(s)

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

def funk(n, target):
    i = 1
    while i <= n:
        if primes(i) >= target and primes(i + 1) >= target and primes(i + 2) >= target and primes(i + 3) >= target:
            return i
        i += 1




print(funk(500000, 4))

# print(prime_factors(20233))

# print(primes(81))
