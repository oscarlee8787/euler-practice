'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''
def prime():
    '''for every number i, if 2 till i**0.5 != 0, i is a prime'''
    prime_list = []
    for i in range(2,300000):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                count += 1
        if count == 1:
            prime_list.append(i)
        if len(prime_list) >= 10001:
            break

    print(prime_list[10000])
    return

prime()
