# Functional Spec's
# 1. Prompt the User to enter a file name
# 2. Print the letter histogram for each letter in the file
# 3. Print the word histogram for each letter in the file

# Imports

# Functions

def read_file(file_name):
    with open(file_name, 'r') as file_handle:
        file_data = file_handle.read()
        return file_data

def letter_histogram(file_data):
    return_dictionary = {}
    file_data = file_data.lower()
    for char in file_data:
        if char not in return_dictionary:
            # initialize the tally for this dictionary entry as 1
            return_dictionary[char] = 1
        else:
            # increment the tally for this dictionary entry
            return_dictionary[char] += 1
    return return_dictionary

def word_histogram(file_data):
    return_dictionary = {}

    file_data = file_data.lower()
    word_list = []
    word_list = file_data.split(" ")

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

    # Prompt the User for a file name
    file_name = input("Please enter a file name: ")

    # Read the file to get the data
    file_data = read_file(file_name)

    # Print the letter histogram for the file
    print_letter_histogram = letter_histogram(file_data)
    print(print_letter_histogram)

    # Print the word histogram for the file
    print_word_histogram = word_histogram(file_data)
    print(print_word_histogram)
    
