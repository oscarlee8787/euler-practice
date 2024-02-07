'''
How many different ways can £2 (200p) be made using any number of coins?
'''

# coins = [1,2,5,10,20,50,100,200]

# # for a given number n, deduct coin for coin in coins <= n

# def count_times(num):
#     filter_a = filter(lambda x: x < num, coins)
#     for coin in list(filter_a):
#         while num -
#         print(num - coin)


# count_times(10)

# 5:
#     5:-2-2-1
#     5:-2-1-1-1
#     5:-1-1-1-1-1

# 10: 10-10=0
#     10-5-5=0
#     10-5-2-2-1
#     10-5-
# 20: 10 10
# 50: 20, 20, 10

start = 5
denom = [5,2,1]

def count_d(num):
    count = 0
    for i in denom:
        if num - i == 0:
            count += 1
        else:
            count_d(num - i)

    print(count)
    return

count_d(5)
