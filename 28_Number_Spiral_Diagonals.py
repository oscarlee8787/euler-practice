'''What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?'''

# 1
# 3 5 7 9
# 13 17 21 25
# 31 37 43 49


# 1+3**2+5**2+7**2

#     9*3 - 2*6 + 25*3 - 4*6 + 49*3 - 6*6

# 9 + 9-2 + 9-4 + 9-6
# 25 + 25-4 + 25-8 + 25-12

# 25 + 25*3-4*6

def solver(side):
    '''solved by listing out the numbers that need to be added and subtracted and finding the pattern'''
    sum = 1
    for i in range(3, side+1, 2):
        sum += i**2
        sum = sum + i**2*3 - (i-1)*6
    return sum

print(solver(1001))
