# Functional Spec's
# 1. Prompt the User to enter a file name
# 2. Prompt the User to enter the contents of the file
# 3. Save the contents to the file

# Imports

# Functions

def write_file(file_name, data):
    with open(file_name, 'w') as file_handle:
        file_handle.write(data)

def read_file(file_name):
    with open(file_name, 'r') as file_handle:
        contents = file_handle.read()
        print(contents)

# Main

if __name__ == "__main__":

    file_name = input("Please enter a file name: ")
    data = input("Please enter data: ")
    # Write data to file
    write_file(file_name, data)
    # Print the contents of the file to make sure it worked correctly
    read_file(file_name)
