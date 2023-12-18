'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
'''
def max_prime(input_num):
    #create a list of factors by finding numbers within range for which modulo == 0
    list_all = []
    for i in range(1, input_num):
        if input_num%i == 0:
            list_all.append(i)
    # print(list_all)
    #for every item in list, verify if it is prime by checking if 1 and itself are the only factors
    ver_list = []
    for num in list_all:
        count = 0
        for i in range(1, int(num/2)+1):
            if num%i == 0:
                count += 1
        if count > 1:
            break
        ver_list.append(num)
    # print(ver_list)
    #return largest from this verified list
    return max(ver_list)

# print(max_prime(13195))


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:     #if i is not a factor of n
            i += 1    #i = i + 1
        else:         #if i is a factor of n
            n //= i   #n = n/i
    return n

print(largest_prime_factor(600851475143))
