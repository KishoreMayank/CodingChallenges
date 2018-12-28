'''
Rotate Matrix:
    Rotate an image by 90 degrees clockwise
'''

def rotate_matrix(matrix):
    for layer in range(len(matrix) // 2): # // is integer division
        last = len(matrix) - layer - 1 # the last element in the row that needs to be rotat
        for i in range(layer, last):
            offest = i - layer # the element in that layer
            
            # save top
            top = matrix[layer][i] 

            # left -> top
            matrix[layer][i] = matrix[last - offest][layer]

            # bottom -> left
            matrix[last - offest][layer] = matrix[last][last - offest]

            # right -> bottom
            matrix[last][last - offest] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix