# Imports

import matplotlib.pyplot as plot

# Functions

def f(x):
    x = x + 1
    return x

def plotit():
    xs = list(range(-3, 4))
    ys = []
    for x in xs:
        ys.append(f(x))

    plot.plot(xs, ys)
    plot.show()

# Main

if __name__ == "__main__":

    plotit()
