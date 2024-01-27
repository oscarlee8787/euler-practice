'''A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 =0.(3)
1/4 =0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
# find n in n < 1000 where 1/n

# The length of the repetend (period of the repeating decimal segment) of 1/p
# is equal to the order of 10 modulo p.
# example:
# l(3) == 1 --> (10^1) % 3 == 1
# l(7) == 6 --> (10^6) % 7 == 1
# l(14) == 6 --> (10^6) % 14 ==
# 10**k - 1 % denominator == 0

# print(1/7)
# print(10//7)
# # 10-7=3
# print(30//7)
# # 30-28-2
# print(20//7)
# # 20-14=6
# print(60//7)

def repeating_cycle(denom, num=1):
    remainders = []
    rems = None
    while rems not in remainders:
        remainders.append(rems)
        num *= 10
        rems = num % denom
    remainders.pop(0)
    return len(remainders)

length = {}

for i in range(1, 1000): # create a dict for numbers from 1 to 999, its corresponding number of repeating cycle
    length[i] = repeating_cycle(i)

print(max(length, key=length.get)) # find in dictionary, the key that has the greatest value
