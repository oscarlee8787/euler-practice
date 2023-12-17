'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
'''

#create a list of factors by finding numbers within range for which modulo == 0
list_all = []
for i in range(13195):

#for every item in list, verify if it is prime by checking if 1 and itself are the only factors
#return largest from this verified list
