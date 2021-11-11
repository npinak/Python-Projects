'''Write a single program in Python that checks the spelling of the first chapter of
“Alice In Wonderland.” First use a linear search, then use a binary search.
Print the line number along with the word that does not exist in the dictionary.'''

import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


# Reading the dictionary file

dictionary_file = open("dictionary.txt")

dictionary_list = []

for word in dictionary_file:
    word = word.strip()
    dictionary_list.append(word)

dictionary_file.close()


##### Doing the linear search #####
'''
print("--- Linear Search ---")


story_file = open("AliceInWonderLand200.txt")

word_list = []

for line in story_file:
    word_list = split_line(line)
    for word in word_list:
        current_list_position = 0
        while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
            current_list_position += 1
        if current_list_position == len(dictionary_list):
            print(word)
        else:
            continue
'''
print("--- Binary Search ---")





