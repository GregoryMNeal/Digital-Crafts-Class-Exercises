# Functional Spec's:
# 1. Print Elizabeths' phone number
# 2. Add a entry to the dictionary: Kareem's number is 938-489-1234
# 3. Delete Alice's phone entry
# 4. Change Bob's phone number to '968-345-2345'
# 5. Print all phone entries

# Imports

# Functions

# Add a dictionary entry
def add_dictionary_entry(dictionary_key, dictionary_value):
    phonebook_dict[dictionary_key] = dictionary_value

# Change a dictionary entry
def chg_dictionary_entry(dictionary_key, dictionary_value):
    phonebook_dict[dictionary_key] = dictionary_value

# Delete a dictionary entry
def del_dictionary_entry(dictionary_key):
    del phonebook_dict[dictionary_key]

# Retrieve a dictionary entry
def get_dictionary_entry(dictionary_key):
    return_dict_value = phonebook_dict.get(dictionary_key)
    return return_dict_value

# Main

if __name__ == "__main__":

    phonebook_dict = {
      'Alice': '703-493-1834',
      'Bob': '857-384-1234',
      'Elizabeth': '484-584-2923'
    }

    # Satisfy Functional Spec #1
    dictionary_key = 'Elizabeth'
    phone = get_dictionary_entry(dictionary_key)
    print("{name}'s phone number is {phone}.".format(name=dictionary_key, phone=phone))

    # Satisfy Functional Spec #2
    dictionary_key = 'Kareem'
    dictionary_value = 'Kareem\'s number is 938-489-1234'
    add_dictionary_entry(dictionary_key, dictionary_value)
    test = get_dictionary_entry(dictionary_key)
    print(test)

    # Satisfy Functional Spec #3
    dictionary_key = 'Alice'
    del_dictionary_entry(dictionary_key)
    test = get_dictionary_entry(dictionary_key)
    print(test)

    # Satisfy Functional Spec #4
    dictionary_key = 'Bob'
    dictionary_value = '968-345-2345'
    chg_dictionary_entry(dictionary_key, dictionary_value)
    test = get_dictionary_entry(dictionary_key)
    print(test)

    # Satisfy Functional Spec #5
    for dictionary_key in phonebook_dict.keys():
        print(phonebook_dict[dictionary_key])
