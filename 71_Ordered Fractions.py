
##### SOLUTION 1 #####

print(999999//7*3-1)

##### SOLUTION 2 #####
from math import gcd

def reduced_denum(a,b):
    return int(a/gcd(a,b)), int(b/gcd(a,b))

# print(reduced_denum(10,8))

d = 1000000
for difference in reversed(range(d+1)):
    num = 3 * difference
    denum = 7 * difference
    num -= 1
    num, denum = reduced_denum(num, denum)
    if denum <= d:
        print(f"{num}/{denum}")
        break
