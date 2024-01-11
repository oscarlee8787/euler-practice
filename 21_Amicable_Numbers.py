'''Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b,
then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.'''

# from 2 till 10000:
    # find list of divisors for each number

# pair number with divisor list sum in dict

divisor_dict = {}
for i in range(2, 10000):
    divisor_list = []
    for j in range(1,i):
        if i%j == 0:
            divisor_list.append(j)
    divisor_dict[i] = sum(divisor_list)

# for every ele in dict:
    # if dict[key] == dict[dict[key]]:
        # both are amicable numbers

amicable_list = []
for ele in divisor_dict:
    # print(ele)
    # print(divisor_dict[ele])
    # print(divisor_dict[divisor_dict[ele]])
    try:
        if ele == divisor_dict[divisor_dict[ele]] and ele != divisor_dict[ele]:
            amicable_list.append(ele)
            amicable_list.append(divisor_dict[ele])
    except:
        continue

print(sum(set(amicable_list)))
