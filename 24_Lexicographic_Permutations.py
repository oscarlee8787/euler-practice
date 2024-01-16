'''A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
# generate list permutations of numbers
# sort in ascending order
# return the millionth value of the given digits

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_list = []

def permutation(a, size):
    if size == 1:
        number = ''.join(map(str, a))
        permutation_list.append(int(number))

    for i in range(size):
        permutation(a, size-1)

        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size%2 == 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]

size = len(list_)
permutation(list_, size)
permutation_list.sort()
print(permutation_list[999999])
