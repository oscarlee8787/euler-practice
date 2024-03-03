'''An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910 1 112131415161718192021
It can be seen that the 12 digit of the fractional part is 1.
If d_n represents the n digit of the fractional part, find the value of the following expression.
d_1  d_{10}  d_{100}  d_{1000}  d_{10000}  d_{100000}  d_{1000000}'''

s = ''

for i in range(1,1000001):
    s += str(i)

ans = 1
for i in range(0, 6):
    ans *= int(s[10**i - 1])

print(ans)
