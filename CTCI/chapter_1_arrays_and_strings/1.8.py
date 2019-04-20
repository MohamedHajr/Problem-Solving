def clear_row(index, matrix):
    n = len(matrix[0])
    for i in range(n):
        matrix[index][i] = 0

def clear_column(index, matrix):
    m = len(matrix)
    for i in range(m):
        matrix[i][index] = 0

def zero_matrix(matrix):
    zeros = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                result.append((i, ))
    for result in zeros:
        clear_row(result[0], matrix)
        clear_column(result[1], matrix)
