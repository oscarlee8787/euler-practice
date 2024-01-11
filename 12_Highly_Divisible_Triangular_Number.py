'''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:

 1 : 1
 3 : 1,3
 6 : 1,2,3,6
10 : 1,2,5,10
15 : 1,3,5,15
21 : 1,3,7,21
28 : 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
'''

# find very big list of triangle numbers
triangle_list = []
number = 0

for i in range(1,20000):
    number += i
    triangle_list.append(number)
# print(triangle_list)

# for every number, count number of divisors
    # i from 1 to n^0.5, if i%==0, i is a divisor of n
# save divisors to a list
# count number of divisors and save to a dictionary
# with the triangle number as key and number of divisors as value
found = False
for number in triangle_list:
    divisor_list = []
    for i in range(1,int(number**0.5)+1):
        if number % i == 0:
            divisor_list.append(i)
            divisor_list.append(int(number/i))
    if len(divisor_list) > 500:
        # print(divisor_list)
        print(number)
        found = True
        break

if not found:
    print("didn't find number")


# return first key with value > 500
