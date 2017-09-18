# Imports

# Functions

def find_smallest():
    numbers = [1,2,5,4,3]
    # Find the largest number first
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    # Find the smallest number
    smallest = largest
    for i in numbers:
        if i < smallest:
            smallest = i
    # Print the smallest number
    print(smallest)

# Main

if __name__ == "__main__":

    find_smallest()
