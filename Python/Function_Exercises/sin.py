# Imports

import math
import matplotlib.pyplot as plot

# Functions

def f(x):
    s = math.sin(x)
    return s

def plotit():
    xs = list(range(-5, 6))
    ys = []
    for x in xs:
        ys.append(f(x))

    plot.plot(xs, ys)
    plot.show()

# Main

if __name__ == "__main__":

    plotit()
