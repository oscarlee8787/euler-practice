'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def largest():
    '''
    product of 2 3-digit numbers has 5 or 6 digits
    find a 5 or 6 digit number with 2 factors of 3 digits

    999999, 998899
    '''
    # create a list of palindromic numbers
    pal_num = []
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                number = 100000*i + 10000*j + 1000*k + 100*k + 10*j + i
                pal_num.append(number)
    # check each element for 2 factors of 3 digits
    for ele in reversed(pal_num):
        for i in range(100,1000): # create a loop of all 3-digit numbers
            if not ele % i: # if ele is divisable by a 3-digit
                if len(str(int(ele/i))) == 3: # check if the result is 3 digit as well
                    print(ele) # return when found
                    return 0

    print('nothing found')
    return 1

largest()
