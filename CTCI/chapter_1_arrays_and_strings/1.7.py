def rotate_matrix_90(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for i in range(len(matrix) - 1):
        top = [0][i]
        left = [n-1-i][0]
        right = [i][n-1]
        bottom = [n-1][n-1-i]
        #start rotatting
        temp = top
        top = left
        left = bottom
        bottom = right
        right = top

        


