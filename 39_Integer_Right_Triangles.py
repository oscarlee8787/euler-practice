'''If p is the perimeter of a right angle triangle with integral length sides,
{a, b, c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p < 1000, is the number of solutions maximised?
'''
# a**2 + b**2 = (120 - a - b)**2
# 2a+c=p
#
# a + b + c = p
# c = p - a - b
# alist = []
count_max = 0
count = 0
for p in range(500):
    for a in range(1,int(p/2)):
        # for b in range(int((p**2 - a**2)**0.5)-1, p-a):
        for b in range(a, p-a):
            # print(b)
            if a**2 + b**2 == (p - a - b)**2:
                count += 1
    if count > count_max:
        count_max = count
                # print(a, b)
print(count_max)
# n = []
# for i in range(500):
#     count = triangles(i)
#     n.append(count)

# print(n)

# print(triangles(00))
