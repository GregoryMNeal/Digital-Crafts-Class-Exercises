# Imports

# Functions

def make_long():
    istring = input("Please enter a string: ")
    v = int(input ("How many vowels would you like? "))
    ustring = istring.upper()
    ustring = ustring.replace("AA", "A" * v)
    ustring = ustring.replace("EE", "E" * v)
    ustring = ustring.replace("II", "I" * v)
    ustring = ustring.replace("OO", "O" * v)
    ustring = ustring.replace("UU", "U" * v)
    pstring = ustring.capitalize()
    print(pstring)

# Main

if __name__ == "__main__":

    make_long()
