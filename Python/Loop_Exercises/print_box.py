# Imports

# Functions

def print_a_box():
    height = int(input("Height? "))
    width = int(input("Width? "))
    top_bottom = "*" * width
    print(top_bottom)
    middle = ' ' * (width - 2)
    for i in range(height - 2):
        print("*" + middle + "*")
    print(top_bottom)

# Main

if __name__ == "__main__":

    print_a_box()
