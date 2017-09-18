# Imports

# Functions

def print_var_triangle():
    height = int(input("What is the height of the triangle? "))
    spaces = height - 1
    asterisks = 1
    for i in range(height):
        print(' ' * spaces, '*' * asterisks)
        spaces = spaces - 1
        asterisks = asterisks + 2

# Main

if __name__ == "__main__":

    print_var_triangle()
