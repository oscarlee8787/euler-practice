'''The 12th term of the Fibonacci sequence, 144, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

# create a list of Fibonacci sequence
# find first term with 1000 digits
# 1, 1, 2, 3, 5, 8, 13...

f_dict = {0:0, 1:1, 2:1}

def fib(n):
    '''returns the n th term of the fib sequence
    but the first term is 1, not 0'''
    if n in f_dict:
        # print(f_dict.values())
        return f_dict[n]

    f_dict[n] = fib(n-1) + fib(n-2)
    return f_dict[n]

for i in range(10000):
    if len(str(fib(i))) == 1000:
        print(i)
        break
    elif i == 9999:
        print('not found')
