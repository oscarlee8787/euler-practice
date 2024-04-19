'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

s = 0
l = []
for i in range(2, 1000000):
    if is_prime(i) is True and (s + i) < 1000000:
        s += i
        l.append(i)
print(s, l)

# print(is_prime(s))

k = 0
while is_prime(s) is False:
    s -= l[k]
    k += 1
print(f"{s} is prime: {is_prime(s)}")

# print(l[k:])
