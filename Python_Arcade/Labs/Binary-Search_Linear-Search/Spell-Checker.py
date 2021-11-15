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

print("--- Linear Search ---")


story_file = open("AliceInWonderLand200.txt")

word_list = []
line_count = 0

for line in story_file:
    word_list = split_line(line)
    line_count += 1
    for word in word_list:
        current_list_position = 0
        while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
            current_list_position += 1
        if current_list_position == len(dictionary_list):
            print(f"Line {line_count} possible misspelled word: {word}")
        else:
            continue


##### Doing the Binary Search #####

print("--- Binary Search ---")


story_file = open("AliceInWonderLand200.txt")

word_list = []
line_count = 0

for line in story_file:
    word_list = split_line(line)
    line_count += 1
    for word in word_list:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False
        while lower_bound < upper_bound and found == False:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos
            else:
                found = True
        if found == False:
            print(f"Line {line_count} possible misspelled word: {word}")
        else:
            continue





