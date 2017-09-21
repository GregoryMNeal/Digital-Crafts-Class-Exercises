# Imports
import json
from matplotlib import pyplot

# Functions

def plot_coordinates(file_data):
    x_coordinates = []
    y_coordinates = []
    for key, value in file_data.items():
        for coordinates in value:
            x_coordinates.append(coordinates[0])
            y_coordinates.append(coordinates[1])
    pyplot.scatter(x_coordinates, y_coordinates)
    pyplot.show()

# Main

if __name__ == "__main__":

    file_name = input('Please enter the name of a JSON file: ')

    file_data = {}
    with open(file_name, 'r') as file_handle:
        file_data = json.load(file_handle)

    plot_coordinates(file_data)
