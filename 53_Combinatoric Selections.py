# from itertools import combinations

# cnt = 0
# for n in range(1, 101):
#     for r in range(1, n//2 + 1):
#         a = combinations(range(n), r)
#         length = len([i for i in a])
#         if length > 1000000:
#             cnt += (n - r - r + 1)
#             print(n, r)
#             print(cnt)
#             break
# print(cnt)

def fact(n, r):
    lower = r
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while lower > 0:
            fact *= n
            fact /= lower
            n -= 1
            lower -= 1

        return fact

# print(fact(23, 10))

cnt = 0
for n in range(1, 101):
    for r in range(1, n//2 + 1):
        if fact(n, r) > 1000000:
            cnt += (n - r - r + 1)
            # print(n, r)
            # print(cnt)
            break
print(cnt)


# n!
# r! * (n-r)!
