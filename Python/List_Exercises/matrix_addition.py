# Imports

# Functions

def add_matrices():
    matrix1 = [ [1, 3],
                [2, 4] ]
    matrix2 = [ [5, 2],
                [1, 0] ]
    result =  [ [0, 0],
                [0, 0] ]
    # iterate through rows
    for x in range(len(matrix1)):
        # iterate through columns
        for y in range(len(matrix1[0])):
            result[x][y] = matrix1[x][y] + matrix2[x][y]
    print(result)

# Main

if __name__ == "__main__":

    add_matrices()
