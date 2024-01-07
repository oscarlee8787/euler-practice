'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''
# define function if n is even: n/2, else: 3n + 1
# return number of calculations
# for range 1000000 store all results of function in a list
# return index of highest number in list

def collatz(n):
    count = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count

term_list = []

for i in range(1, 1000000):
    term = collatz(i)
    term_list.append(term)

print(term_list.index(max(term_list)))
