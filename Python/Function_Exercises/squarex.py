# Imports

import matplotlib.pyplot as plot

# Functions

def f(x):
    # return the square of x
    sq = x * x
    return sq

def plotit():
    xs = list(range(-100, 101))
    ys = []
    for x in xs:
        ys.append(f(x))

    plot.plot(xs, ys)
    plot.show()

# Main

if __name__ == "__main__":

    plotit()
