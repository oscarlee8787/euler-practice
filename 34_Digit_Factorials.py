'''Find the sum of all numbers which are equal to the sum of the factorial of their digits.
1! and 2! do not count.
'''

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * factorial(n-1)

nums = []

for i in range(3, 2000000):
    digits = [a for a in str(i)]
    factsum = 0
    for digit in digits:
        fact = factorial(int(digit))
        factsum += fact
    if i == factsum:
        nums.append(i)

print(nums)
# print(factorial(3))
