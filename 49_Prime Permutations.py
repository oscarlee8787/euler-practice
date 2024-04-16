'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways:

(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from itertools import combinations, permutations

def prime_list(m, n):
    ans = []
    for i in range(m, n + 1):
        if is_prime(i)is True:
            ans.append(i)
    return ans

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(prime_list(1000, 9999))

_list = prime_list(1000,9999)
_set = set(_list)

# a = permutations('8147')
# y = [''.join(i) for i in a]

# for n in _list:
#     a = permutations(str(n))
#     y = set([''.join(i) for i in a])
#     if len(y&_set) == 3:
#         print(y&_set)

# # print(set(y))
# # print(_set)
for n in _list:
    if (n + 3330 in _set) and (n + 6660 in _set):
        if set(str(n)) == set(str(n+3330)) == set(str(n+6660)):
            print(n, n+3330, n+6660)
