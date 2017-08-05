wordlist = open('113809of.fic').readlines()

'''
use str.count() method to check how many 'a's and 'e's are in a word.

using for loop, going though each word, each character looking for a and e. use counter.

'''
count = 0
for word in wordlist:
    if word.count('a') == 2 and word.count('e') == 0:
        print(word)
        count += 1
print(f'total number of the words meeting the criteria is {count}')
