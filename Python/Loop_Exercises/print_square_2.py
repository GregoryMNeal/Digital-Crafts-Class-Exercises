# Imports

# Functions

def print_var_square():
    size = int(input("How big is the square? "))
    square = "*" * size
    for i in range(size):
        print(square)

# Main

if __name__ == "__main__":

    print_var_square()
