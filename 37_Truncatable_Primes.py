'''The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

ans = 0

for i in range(13, 999999, 2):
    i = str(i)
    if i[0] == '9' or i[-1] == '9':
        continue
    length = len(i)
    k = 0
    num = i
    ri = i
    broke = False
    while k < length:
        if is_prime(i) is False:
            broke = True
            break
        if is_prime(ri) is False:
            broke = True
            break
        i = i[1:]
        ri = ri[:-1]
        k += 1

    if broke is False:
        print(num)
        ans += int(num)

print(f'Sum is: {ans}')
