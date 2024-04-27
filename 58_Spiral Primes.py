def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

# print(is_prime(31))
3, 5, 7, 9, 13, 17, 21, 25

def func(limit):
    pos = 1
    prime = 0
    layer = 1
    cnt = 1
    while pos < limit:
        for _ in range(4):
            pos += (2 * layer)
            cnt += 1
            if is_prime(pos) is True:
                prime += 1
        layer += 1
        if prime / cnt < 0.1 and layer > 3:
            print(f"ratio: {(prime / cnt)}")
            print(f"prime: {prime}")
            print(f"pos:{pos}")
            return pos**0.5

    return -1

print(func(10000000000))
# print(func(49))
