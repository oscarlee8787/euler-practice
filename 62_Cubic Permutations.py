cnt = dict()


for i in range(1, 50000):
    n = ''.join(sorted(str(i**3)))
    if n not in cnt:
        cnt[n] = 0
    cnt[n] += 1
    # if cnt[n] == 5:
    #     print(n, i)
for i, v in enumerate(cnt.values()):
    if v ==5:
        print(i, v)


# for i in range(1, 20000):
#     k = str(i**3)
#     n = ''.join(sorted(k))
#     if n == '1123445567899':
#         print(n, i)
