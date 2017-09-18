# Imports

import matplotlib.pyplot as plot

# Functions

def f(x):
    if x == 0:
        x = -1
    else:
        rem = x % 2
        # check for odd for even
        if rem != 0:
            x = 1
        else:
            x = -1
    return x

def plotit():
    xs = list(range(-5, 6))
    ys = []
    for x in xs:
        ys.append(f(x))

    plot.bar(xs, ys)
    plot.show()

# Main

if __name__ == "__main__":

    plotit()
