from itertools import combinations

cnt = 0
for n in range(1, 101):
    for r in range(1, n//2 + 1):
        a = combinations(range(n), r)
        length = len([i for i in a])
        if length > 1000000:
            cnt += (n - r - r + 1)
            print(n, r)
            print(cnt)
            break
print(cnt)


# 23 - 10 = 13

# 10, 11, 12, 13

# 13 - 10 + 1
