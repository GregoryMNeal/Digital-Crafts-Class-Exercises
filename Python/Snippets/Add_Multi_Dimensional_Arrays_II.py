
matrix1 = [ [1, 3], [5, 2] ]
matrix2 = [ [2, 4], [1, 0] ]

answer_matrix = []
for index1 in range(0, len(matrix1)):
    for index2 in range(0, (len(matrix1[index1]))):
        answer = (matrix1[index1][index2] + matrix2[index1][index2])
        answer_matrix.append(answer)

print(str(answer_matrix))
