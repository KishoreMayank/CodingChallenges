'''
Rotate Matrix:
    Rotate an image by 90 degrees clockwise
'''

def rotate_matrix(matrix):
    for layer in range(len(matrix) // 2): # // is integer division
        first, last = layer, len(matrix) - layer - 1
        for i in range(first, last):
            offest = i - first
            # save top
            top = matrix[first][i] 

            # left -> top
            matrix[first][i] = matrix[last - offest][first]

            # bottom -> left
            matrix[last - offest][first] = matrix[last][last - offest]

            # right -> bottom
            matrix[last][last - offest] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix