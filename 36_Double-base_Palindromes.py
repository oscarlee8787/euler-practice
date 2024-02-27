'''The decimal number, 585 = 1001001001_2 (binary),
is palindromic in both bases.
Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
def is_palin(n):
    n = str(n)
    half = int(len(n)/2) + 1
    if n[:half] == n[:-half - 1:-1]:
        return True
    return False

ans = []
s = 0

for i in range(1, 1000000, 2):
    b = bin(i)[2:]
    if is_palin(i) is True:
        if is_palin(b) is True:
            ans.append(i)
            s += i

print(ans, s)
