# Functional Spec's
# 1. Write a Function called 'letter_histogram'
# 2. The 'letter_histogram' Function must take a word as input
# 3. The 'letter_histogram' Function must return a dictionary containing
#       the tally of how many times each letter in the alphabet was used in
#       the word.

# Imports

# Functions

def letter_histogram(word):
    return_dictionary = {}
    for char in word:
        if char not in return_dictionary:
            # initialize the tally for this dictionary entry as 1
            return_dictionary[char] = 1
        else:
            # increment the tally for this dictionary entry
            return_dictionary[char] += 1
    return return_dictionary

# Main

if __name__ == "__main__":

    word = input("Please enter a word: ")
    letter_dictionary = letter_histogram(word)
    print(letter_dictionary)
