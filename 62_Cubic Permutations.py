cnt = dict()
first = dict()


for i in range(1, 50000):
    k = str(i**3)
    n = ''.join(sorted(k))
    if n not in cnt:
        cnt[n] = 0
        first[n] = i
    cnt[n] += 1


ans = (first[list(cnt.keys())[list(cnt.values()).index(5)]])
print(ans)
print(ans**3)
