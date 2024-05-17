k = 1
cnt = 0
for n in range(1,100):
    for d in range(1,100):
        if len(str(n ** d)) == d:
            cnt += 1
            print(f"{n}**{d} is {n**d} length: {d}")
print(cnt)
