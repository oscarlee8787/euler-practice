'''Find the sum of all the numbers
that can be written as the sum of fifth powers of their digits.'''

def is_sum_fifth(num):
    num_list = [int(x) for x in list(str(num))]
    num_sum = 0
    for n in num_list:
        num_sum += n**5
    if num == num_sum:
        # print(True)
        return True
    else:
        # print(False)
        return False

ans_list = []
for i in range(10, 1000000):
    if is_sum_fifth(i):
        ans_list.append(i)

print(sum(ans_list))
