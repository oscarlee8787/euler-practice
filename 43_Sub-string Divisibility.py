'''The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_{10}=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
'''1, 2, 3



'''

from itertools import permutations

def pandigitals():
    digits = '0123456789'
    pandigits = [''.join(d) for d in permutations(digits)]
    # for num in pandigits:
    #     if num[]
    return pandigits[9*8*7*6*5*4*3*2:]

pandigits = pandigitals()

ans = 0
for num in pandigits:
    if int(num[1:4]) % 2 == 0 and int(num[2:5]) % 3 == 0 and int(num[3:6]) % 5 == 0 and int(num[4:7]) % 7 == 0 and int(num[5:8]) % 11 == 0 and int(num[6:9]) % 13 == 0 and int(num[7:]) % 17 == 0:
        ans += int(num)

print(ans)
