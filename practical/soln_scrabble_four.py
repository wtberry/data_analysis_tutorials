# Using file 113809of.fic identify how many words have:
# identify the count of letters in the words:
# 1. which three letters appear most/least frequently
# 1. which which letter occurs most frequently as a double (i.e. 'ee', 'oo', etc)

import pprint

fin = open('113809of.fic').readlines()

terms = []
for line in fin:
    terms.append(line.strip())

letters = {}
for term in terms:
    for letter in term:
        letters[letter] = letters.get(letter, 0) + 1

highest = ['', 0]
second_highest = ['', 0]
third_highest = ['', 0]

lowest = ['', 113809]
second_lowest = ['', 113809]
third_lowest = ['', 113809]


for letter, count in letters.items():
    if count > highest[1]:
        third_highest = second_highest
        second_highest = highest
        highest = [letter , count]
    elif count > second_highest[1]:
        third_highest = second_highest
        second_highest = [letter, count]

    if count < lowest[1]:
        third_lowest = second_lowest
        second_lowest = lowest
        lowest = [letter , count]

    elif count < second_lowest[1]:
        third_lowest = second_lowest
        second_lowest = [letter, count]





print(highest, second_highest, third_highest, sep='\n')
print()
print(third_lowest, second_lowest, lowest, sep='\n')
print()
pprint.pprint(letters)

digraphs = []
for term in terms:
    for start in range(len(term) - 1):

        digraph = term[start:start+2]
        if len(digraph) == 2:
            if digraph[0] == digraph[1]:
                digraphs.append(digraph)

digraph_count = {}
for digraph in digraphs:
    digraph_count[digraph] = digraph_count.get(digraph, 0) + 1

highest_double = ''
highest_double_count = 0
for dg, count in digraph_count.items():
    if count > highest_double_count:
        highest_double_count = count
        highest_double = dg

print(highest_double)
pprint.pprint(digraph_count)
