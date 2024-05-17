# find prime closest to 1 000 000
# import time
# start = time.time()

def sieve(n):
    list_ = []
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i, isprime in enumerate(p):
        if isprime:
            # print(i)
            list_.append(i)
            for k in range(i*i, (n+1), i):
                p[k] = False
    return list_

sieve = sieve(10000)
ans = 1
for i in sieve:
    if ans*i > 1000000:
        print(ans)
        break
    ans *= i

# end = time.time()
# print(f"1st: {end-start:.8f}")


# start = time.time()
# def sieve2(n):
#     multiples = set()
#     for i in range(3, n+1, 2):
#         if i not in multiples:
#             # print(i)
#             for j in range(i*i, n+1, i):
#                 multiples.add(j)
# sieve2(80)
# end = time.time()
# print(f"2nd: {end-start:.8f}")
# import math

# # print(math.gcd(999984, 1))
# max_ = 0
# ans = 0
# for i in range(1000000, 0, -2):
#     cnt = 0
#     for j in range(2, i):
#         if math.gcd(i,j) == 1:
#             cnt += 1
#     if cnt > max_:
#         max_ = cnt
#         ans = i
#     if i == 999800:
#         print(max_)
#         print(ans)
#         break
# print(cnt)
