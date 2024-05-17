### SOLUTION 1 (TOO SLOW) ###
from math import gcd

cnt = 0
for i in range(10000):
    j = 1
    while j < i:
        if gcd(i, j) == 1:
            cnt += 1
        j += 1
print(cnt)
