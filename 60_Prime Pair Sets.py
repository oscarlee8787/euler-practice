from itertools import permutations

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_list = []

for i in range(2, 300000):
    if is_prime(i) is True and str(i)[-1] != "5":
        prime_list.append(i)

# print(prime_list)

a = ['3','7','109','673']
# b = 7
# c = 109
# d = 673

for k in prime_list:
    broke = False
    if k > 673:
        for org in a:
            n1 = org + str(k)
            n2 = str(k) + org
            if is_prime(int(n1)) is False or is_prime(int(n2)) is False:
                broke = True
                break
        if broke is False:
            print(k)
            break
