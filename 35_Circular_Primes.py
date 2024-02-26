'''The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

def is_prime(n):
    '''for every number i, if 2 till i**0.5 != 0, i is a prime'''
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# list of primes below one million
# loop through list, if all rotations are within list, number is circular


prime_set = set()
for i in range(2, 1000000):
    if is_prime(i):
        prime_set.add(str(i))

count = 0

for i in prime_set:
    n = str(i)
    length = len(i)
    is_circular = True
    for j in range(length):
        i = i[1:] + i[0:1]
        if i not in prime_set:
            is_circular = False
            break
    if is_circular:
        count += 1

print(count)
