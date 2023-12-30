'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
2000000
'''
def primess():
    '''
    finds all primes below two million and save to list
    returns the sum of the list
    '''
    list_ = []
    for i in range(2, 2000000): # finding primes from 1 - 200
        count = 0
        for j in range(1, int(i**0.5)+1): # if i is divisable by numbers from 1 to i^0.5
            if i%j == 0:
                count += 1
                if count > 1:
                    break # if more than 1 number can be divided without residual, i is not a prime
        if count == 1:
            list_.append(i) # add i to list of primes if count ==1 at end of prime test

    print(sum(list_))
    return

primess()
