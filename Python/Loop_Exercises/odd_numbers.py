# Imports

# Functions

def odd_numbers():
    for i in range(10):
        rem = i % 2
        if rem != 0:
            print(i)

# Main

if __name__ == "__main__":

    odd_numbers()
