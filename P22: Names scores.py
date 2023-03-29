'''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''

import csv

with open('p022_names.txt') as file:
    reader = csv.reader(file)
    for row in reader:
#        print(row)
        names = row

#print(names)

list.sort(names)

print(names)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

max_score = 0
counter = 1
score_total = 0
for name in names:
    name_score = 0
    for char in name:
        for i in range(26):
            if char == letters[i]:
                name_score += i+1
    name_score = counter*name_score
    if name_score > max_score:
        max_score = max(max_score, name_score)
        print('the largest name score is', max_score, 'with name', name)
    score_total += name_score
    counter+=1

print('the total of all name scores is', score_total)