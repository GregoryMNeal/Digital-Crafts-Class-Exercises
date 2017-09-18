# Imports

# Functions

def add_matrices():
    matrix1 = [ [1, 3],
                [2, 4] ]
    matrix2 = [ [5, 2],
                [1, 0] ]
    # iterate through rows
    dim1 = []
    for x in range(0, len(matrix1)):
        # iterate through columns
        dim2 = []
        for y in range(0, (len(matrix1[x]))):
            result = matrix1[x][y] + matrix2[x][y]
            dim2.append(result)
        dim1.append(dim2)
    print(dim1)

# Main

if __name__ == "__main__":

    add_matrices()
