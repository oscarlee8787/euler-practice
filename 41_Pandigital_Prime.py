'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
'''

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# for i in range(100000001, 1, -1):
#     if len(str(i)) < 9:
#         break
#     str_set = set(str(i))
#     if len(str(i)) == len(str_set) and len(str(i)) == 9 and '0' not in str_set:
#         if is_prime(i) is True:
#             print(i)
#             break

for i in range(10000000, 1, -1):
    str_set = set(str(i))
    if len(str_set) == len(str(i)) and int(max(str(i))) == len(str_set) and '0' not in str_set:
            if is_prime(i) is True:
                print(i)
                break
