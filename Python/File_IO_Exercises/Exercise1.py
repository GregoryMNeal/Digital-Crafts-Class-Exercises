# Functional Spec's
# 1. Prompt the User to enter a file name
# 2. Read the contents of the file and print to screen

# Imports

# Functions

def read_file(file_name):
    with open(file_name, 'r') as file_handle:
        contents = file_handle.read()
        print(contents)

# Main

if __name__ == "__main__":

    file_name = input("Please enter a file name: ")
    read_file(file_name)
