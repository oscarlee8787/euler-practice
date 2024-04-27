from itertools import permutations
with open('resources/0059_cipher.txt') as t:
 text = t.read().replace('"','').split(sep=',')


combi = permutations([ c for c in range(ord('a'), ord('z')+1)], 3)
codes = [a for a in combi]
# print(len(codes))


c = 0
for k in range(len(codes)):
    sum_ = 0
    ans = ""
    for i in text:
        s = int(i)^codes[k][c]
        new_char = chr(s)
        if new_char in {"#", "$", "%", "=", "{", "~", "|", "^", "}"}:
            break
        ans += new_char
        sum_ += s
        c += 1
        c = c % 3
    if len(ans) == 1455:
        print(ans)
        print()
        print(k)
        print(codes[k])
        print(f"The sum is: {sum_}")
        print()

# sum_ = 0
# n = 0
# m = ""
# for i in text:
#     s = int(i)^[120,112,101][n]
#     # print(codes[14164][n])
#     sum_ += s
#     m += chr(s)
#     print(m)
#     n += 1
#     n = n % 3
# print(f"The sum is: {sum_}")
# print(m)
# # print(codes[14164])
