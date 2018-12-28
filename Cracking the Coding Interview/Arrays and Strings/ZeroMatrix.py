'''
Zero Matrix:

'''

def zero_matrix(matrix):
    rowHasZero = False
    colHasZero = False

    for i in range(len(matrix)): # keep track of whether the first col has a 0
        if matrix[i][0] == 0:
            colHasZero = True
            break

    for j in range(len(matrix[0])): # keep track of whether the first row has a 0
        if matrix[0][j] == 0:
            rowHasZero = True
            break

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])): # go through and set the first [row][col] as 0 to nullify
            if matrix[x][y] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for row in range(1, len(matrix)): # nullify the rows with 0s
        if matrix[row][0] == 0:
            nullify_row(matrix, row)

    for col in range(1, len(matrix[0])): # nullify the cols with 0s
        if matrix[0][col] == 0:
            nullify_row(matrix, col)

    if (rowHasZero):
        nullify_row(matrix, 0)
    
    if (colHasZero):
        nullify_col(matrix, 0)

    return matrix

def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0