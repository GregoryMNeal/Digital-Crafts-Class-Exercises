# Imports

# Functions

def rev_string():
    istring = input("Please enter a string: ")
    rlist = []
    for char in reversed(istring):
        rlist.append(char)
    pstring = ''.join(rlist)
    print(pstring)

# Main

if __name__ == "__main__":

    rev_string()
