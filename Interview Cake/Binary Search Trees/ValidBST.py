'''
Valid BST:
    Validate if a Binary Tree is a BST
'''

def bst(root, mini = -float('inf'), maxi = float('inf')):
    if not root:
        return True
    if root.value < mini or root.value > maxi: # check if the node is out of bounds
        return False
    return (bst(root.left, mini, root.value - 1) and bst(root.right, root.value + 1, maxi)) # go left and right