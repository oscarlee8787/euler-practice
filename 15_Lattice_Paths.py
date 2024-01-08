'''Starting in the top left corner of a 2 * 2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 * 20 grid?

1100
1010
1001
0101
0011
0110

000111

'''
# 4*3*2/(2^2)
# (3+3)!/(3! * 3!)

product = 1
for i in range(1,41):
    product *= i

div = 1
for i in range(1,21):
    div *= i

ans = product // div**2

print(ans)
