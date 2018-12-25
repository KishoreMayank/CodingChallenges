'''
Second Largest BST
    Finds the second largest element in a BST
'''

def largest(node):
    while node.right:
        node = node.right
    return node.value

def second_largest(root):
    if not root or (not root.left or not root.right):
        raise ValueError("must be at least 2 nodes")
    
    while root:
        if root.left and not root.right: # traverse all the way to the right
            return largest(root.left)
        if root.right and not root.right.left and not root.right.right: # if not left or right to the right
            return root
        root = root.right