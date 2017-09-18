# Imports

# Functions

def mult_vectors():
    matrix1 = [2,4,5]
    matrix2 = [2,3,6]
    new_matrix = []
    for i in range(0, len(matrix1)):
        new_matrix.append(matrix1[i] * matrix2[i])
    print(str(new_matrix))

# Main

if __name__ == "__main__":

    mult_vectors()
