'''The nth term of the sequence of triangle numbers is given by,
t_n = \frac12n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_{10}.
If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt, a 16K text file containing nearly two-thousand common English words,
how many are triangle words?'''

words = open('resources/0042_words.txt').read().replace('"','').split(sep=',')
triangle_n = set(int(0.5*i*(i+1)) for i in range(1, 100))
count = 0
for word in words:
    word_sum = sum([ord(letter)-64 for letter in word])
    if word_sum in triangle_n:
        count += 1

print(count)
