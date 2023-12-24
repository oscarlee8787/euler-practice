'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# def mult():
#     '''returns the smallest positive number that is
#     evenly divisible by all of the numbers from 1 to 20
#     '''
#     list_ = []
#     i = 2
#     while i <= 20: # find all prime numbers from 1 to 20
#         if 20 % i

# multiply all numbers together

from math import gcd
from functools import reduce

def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

# print(lcm(lcm(lcm(1,2),3),4))
# print(reduce(lcm, range(1, 5)))

def smallest_div(a):
    smallest = reduce(lcm, range(1, a+1))
    print(smallest)
    return

smallest_div(20)
