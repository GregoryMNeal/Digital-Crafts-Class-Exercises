# Imports

# Functions

def make_leet():
    istring = input("Please enter text: ")
    ustring = istring.upper()
    ustring = ustring.replace("A", "4")
    ustring = ustring.replace("E", "3")
    ustring = ustring.replace("G", "6")
    ustring = ustring.replace("I", "1")
    ustring = ustring.replace("O", "0")
    ustring = ustring.replace("S", "5")
    ustring = ustring.replace("T", "7")
    print(ustring)

# Main

if __name__ == "__main__":

    make_leet()
