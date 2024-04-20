'''It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''
for i in range(1,1000000):
    if set([k for k in str(i)]) == set([k for k in str(i * 2)]) == set([k for k in str(i * 3)]) == set([k for k in str(i * 4)]) == set([k for k in str(i * 5)]) == set([k for k in str(i * 6)]):
        print(i)
