'''
Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
'''
# create a list of pandigitals from 1 till the greatest possible (4 digits)
# choose from list based on number of digits
# for example: 4 digit number = (3 digit * 2 digit) or (1 digit * 4 digit)
# save answer to a set to prevent duplicates
pandigitals = []
for i in range(1, 10000):
    seen = list()
    broke = 0
    for j in str(i):
        if j in seen:
            broke = 1
            break
        if j == '0':
            broke = 1
            break
        seen.append(j)
    if broke != True:
        pandigitals.append(i)


print(pandigitals)
