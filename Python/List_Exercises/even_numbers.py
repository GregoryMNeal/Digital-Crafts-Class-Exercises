# Imports

# Functions

def print_even():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    # Print only the even numbers
    for i in numbers:
        rem = i % 2
        if rem == 0:
            print(i)

# Main

if __name__ == "__main__":

    print_even()
