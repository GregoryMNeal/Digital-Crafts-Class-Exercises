# Functional Spec's
# 1. Write a Function called 'word_histogram'
# 2. The 'word_histogram' Function must receive a paragraph as input
# 3. The 'word_histogram' Function must return a dictionary containing
#       the tally of how many times each word is used in the paragraph.

# Imports

# Functions

def word_histogram(paragraph):
    return_dictionary = {}

    paragraph = paragraph.lower()
    word_list = []
    word_list = paragraph.split(" ")

    for word in word_list:
        if word not in return_dictionary:
            # initialize the tally for this dictionary entry as 1
            return_dictionary[word] = 1
        else:
            # increment the tally for this dictionary entry
            return_dictionary[word] += 1
    return return_dictionary

# Main

if __name__ == "__main__":

    paragraph = input("Please enter a paragraph: ")
    word_dictionary = word_histogram(paragraph)
    print(word_dictionary)
