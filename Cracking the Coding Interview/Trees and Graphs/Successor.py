'''
Successor:
    Find the next node of a given node in a BST
'''

def inOrderSuccessor(n):
    if n.right:
        n = n.right # if there is a right subtree, find the value by traversing down the left subtree of it
        while n.left:
            n = n.left
        return n

    p = n.parent 
    while p and n != p.right: # if it's on the left, keep going up till the child is the left of the parent
        n = p  
        p = p.parent 
    return p 
