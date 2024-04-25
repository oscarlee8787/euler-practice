a, b = 1, 1
max_ = 0
for a in range(1, 101):
   for b in range(1, 101):
       sum_ = sum([int(i) for i in str(a ** b)])
       if sum_ > max_:
           max_ = sum_


print(max_)
