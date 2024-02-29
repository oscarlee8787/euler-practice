'''If p is the perimeter of a right angle triangle with integral length sides,
{a, b, c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p < 1000, is the number of solutions maximised?
'''
# a**2 + b**2 = c**2

# a + b + c = p
# alist = []
for a in range(1,49):
    for b in range(1,21):
        result = (a ** 2 + b ** 2) ** 0.5
        # print(result)
    if result.is_integer():
        print (result)
