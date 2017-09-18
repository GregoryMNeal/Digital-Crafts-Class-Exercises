# This is a copy of module positive_numbers_2 but named differently
# so it can be referenced quickly in the future :)

# Imports

# Functions

def positive_list():
    numbers = [-1,1,-2,2,-3,3,-4,4,-5,5]
    pos_list = []
    for i in numbers:
        if i > 0:
            pos_list.append(i)
    print(str(pos_list))

# Main

if __name__ == "__main__":

    positive_list()
