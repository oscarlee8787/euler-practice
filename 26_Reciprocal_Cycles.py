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

# a = 10**n
# smallest n where (1/number) - (1/7)*10**n == integer
def rep_len(n):
    for i in range(1,30):
        result = 1/n - 1/n*10**i
        print(result)
        print(str(result)[-5:-1])
        if str(result)[-5:-1] == '9999' or result.is_integer():
            # print(str(result)[-5:])
            print(i)
            break
        # print(round(result, 4))
        # if result


rep_len(43)
