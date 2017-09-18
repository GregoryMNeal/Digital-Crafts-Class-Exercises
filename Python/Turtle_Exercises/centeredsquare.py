# Imports

from turtle import *

# Functions

def mySquare():
    # Move into position
    up()
    forward(50)
    left(90)
    forward(50)
    left(90)

    down()

    # draw the square
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

    # continue to display endlessly
    mainloop()

# Main

if __name__ == "__main__":

    mySquare()
