# Imports

# Functions

def multiply_a_list():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    # Multiply numbers in list by factor and insert into new list
    factor = 2
    new_list = []
    for i in numbers:
        new_list.append(i * factor)
    print(str(new_list))

# Main

if __name__ == "__main__":

    multiply_a_list()
