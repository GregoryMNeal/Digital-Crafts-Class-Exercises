# Imports

# Functions

def find_largest():
    numbers = [1,2,5,4,3]
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    print(largest)

# Main

if __name__ == "__main__":

    find_largest()
