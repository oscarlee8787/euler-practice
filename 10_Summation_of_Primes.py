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
    for i in range(1, 200):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                count += 1
            if count > 1:
                break
            list_.append(i)

    print(list_)
    return

primess()
