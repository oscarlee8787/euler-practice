'''
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet, for which a + b + c = 1000.
Find the product abc.
'''
'''
a + b + c = 1000
a^2 + b^2 = c^2
a*b*c = ?
'''
'''
(a+b+c)^2 = a^2+b^2+c^2+2(ab+ac+bc)
        = 2c^2+2(ab+ac+bc)
        =2c^2+2abc(1/a+1/b+1/c)
'''
def find():
    for i in range(1,1000):
        for j in range(1,1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                product = i*j*k
    print(product)
    return

find()
