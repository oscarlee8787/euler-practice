'''Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
'''
names = open('resources/names.txt').read().replace('"','').split(sep=',')
names.sort()

def name_score(word):
    score = 0
    for w in word:
        score += ord(w)-64
    return score

total = 0

for index, name in enumerate(names):
    score = name_score(name)
    total += (index+1) * score

print(total)
