'''If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.'''

num_word_dict = {0:'',1:'one', 2:'two', 3:'three', 4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
100:'hundred'}

total = 0
for i in range(1,1000):
    if i//100: # if larger than 100
        hundred = len(num_word_dict[i//100]) + len(num_word_dict[100])
        i = i%100
        if i > 20:
            ten = len(num_word_dict[i//10*10])
            i = i%10
            unit = len(num_word_dict[i])
            length = hundred + ten + unit + len('and')
        elif i == 0:
            length = hundred
        else:
            length = hundred + len(num_word_dict[i]) + len('and')
        # print(i, length)
        total += length
    elif i>20:
            ten = len(num_word_dict[i//10*10])
            i = i%10
            unit = len(num_word_dict[i])
            length = ten + unit
            # print(i, length)
            total += length
    else:
        length = len(num_word_dict[i])
        # print(i, length)
        total += length

print(total+len('onethousand'))

# print(len(num_word_dict[0]))
