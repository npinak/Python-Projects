# To get the interactive python shell type in "python3 in the terminal"

# Next task, remove brackets if one definition

import json
import difflib
from os import close
import time
from typing import no_type_check
## Loading the data ##
data = json.load(open("/Users/pinaknayak/Documents/Github/Python-Projects/Dictionary/data.json"))


## Create a function to get key input and returns the value. ##


def word_input(word):
	actual_word = ""
	word = word.lower() # Make the function case sensitive
	check = word in data # Check to see if the word exists 
	if check == True:
		actual_word = word
		no_quotes = str(data[word])
		no_quotes = no_quotes.replace("[", "").replace("'",'').replace("]", "") # Removing unnecessary formatting characters
		print("\n\nThe definition of " + actual_word + " is: " + no_quotes+"\n\n")
		time.sleep(5)
		double_check = input("\n\nDo you want to see the definition of another word? Please type 'yes' or 'no': ") # Checking to see if they want to restart the program
		double_check = double_check.lower()
		if double_check == "yes":
			which_word = input("\n\nPlease type out which word you want to see the definition of: ") # Which word? 
			return word_input(which_word)
		elif double_check =="no":
			return print("\n\nThanks for checking me out!\n\n") # If no then Peace!
		elif double_check != "yes" or double_check != "no": # Check if yes or no is actually typed out
			return print("\n\nDon't play games now :)\n\n")	
	elif check == False:
		close_match = difflib.get_close_matches(word, data, cutoff= 0.75) # If word mistyped checked to see what they meant
		close_match = str(close_match)
		close_match = close_match.replace("[", "").replace("'",'').replace("]", "")
		if len(close_match) == 0:
			print("\n\nThat word does not exist. Please double check it.\n\n")
			double_check = input("Do you want to see the definition of another word? Please type 'yes' or 'no': ") # Checking to see if they want to restart the program
			double_check = double_check.lower()
			if double_check == "yes":
				which_word = input("\n\nPlease type out which word you want to see the definition of: ") # Which word?
				return word_input(which_word)
			elif double_check =="no":
				return print("\n\nThanks for checking me out!\n\n") # If no then Peace!
			elif double_check != "yes" or double_check != "no": # Check if yes or no is actually typed out
				return print("\n\nDon't play games now :)\n\n")
		else:
			print("\n\nDid you mean: " + str(close_match) + "? " + "\nPlease type 'yes' or 'no' on the next line.\n\n")
			yes_or_no = input("Please enter yes or no: ")
			yes_or_no = yes_or_no.lower()
			if yes_or_no == "no":
				double_check = input("\n\nDo you want to see the definition of another word? Please type 'yes' or 'no': " ) # Checking to see if they want to restart the program
				double_check = double_check.lower()
				if double_check == "yes":
					which_word = input("\n\nPlease type out which word you want to see the definition of: ") # Input what word they want to see
					word_input(which_word)
				elif double_check =="no":
					return print("\n\nThanks for checking me out!\n\n") # Message if they say no
				elif double_check != "yes" or double_check != "no": # Check if yes or no is actually typed out
					return print("\n\nDon't play games now :)\n\n")
			elif yes_or_no == "yes":
				if yes_or_no == "yes" and len(close_match) == 1:
					actual_word = close_match
					no_quotes = str(data[word])
					no_quotes = no_quotes.replace("[", "").replace("'",'').replace("]", "") # Removing unnecessary formatting characters
					print("\n\nThe definition of " + actual_word + " is: " + no_quotes+"\n\n")
					time.sleep(5)
					double_check = input("Do you want to see the definition of another word? Please type 'yes' or 'no': ") # Checking to see if they want to restart the program
					double_check = double_check.lower()
					if double_check == "yes":
						which_word = input("Please type out which word you want to see the definition of: ") # Which word? 
						return word_input(which_word)
					elif double_check =="no":
						return print("\n\nThanks for checking me out!\n\n") # If no then Peace!
					elif double_check != "yes" or double_check != "no": # Check if yes or no is actually typed out
						return print("\n\nDon't play games now :)\n\n")
				elif yes_or_no == "yes" and len(close_match) > 1:
					word = input("\n\nWhich word is it?\n " + str(close_match)+ ": ") # Checking to see which word it is from the list
					if word in close_match:
						actual_word = word 
						no_quotes = str(data[word])
						no_quotes = no_quotes.replace("[", "").replace("'",'').replace("]", "") # Removing unnecessary formatting characters
						print("\n\nThe definition of " + actual_word + " is: " + no_quotes+"\n\n")
						time.sleep(5)
						double_check = input("Do you want to see the definition of another word? Please type 'yes' or 'no': ") # Checking to see if they want to restart the program
						double_check = double_check.lower()
						if double_check == "yes":
							which_word = input("\n\nPlease type out which word you want to see the definition of: ") # Which word do they want to see? 
							return word_input(which_word)
						elif double_check =="no":
							return print("\n\nThanks for checking me out!\n\n") # If no then Peace!
						elif double_check != "yes" or double_check != "no": # Check if yes or no is actually typed out
							return print("\n\nDon't play games now :)\n\n")
			else:
				return print("\n\nDon't play games now :)\n\n")

word = input("Please enter a word: ")
word_input(word)

#######################
#elif yes_or_no != "yes" or yes_or_no != "no": # Check if yes or no is actually typed out
			#	return print("\n\nDon't play games now :)\n\n")