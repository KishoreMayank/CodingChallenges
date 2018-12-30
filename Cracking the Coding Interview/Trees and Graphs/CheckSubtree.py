'''
Check Subtree:
    Check if T2 is a a subtree of T1
'''

class Node:
       def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preOrder(node, s): # Gets the preorder traveral string adding an X for None
    if node == None:
        s = s + 'X'
        return
    s = s + str(node.data) # Add root
    preOrder(node.left, s) # Add left node
    preOrder(node.right, s) # Add right node

def containsTree(t1, t2):
    s1 = ''
    s2 = ''

    preOrder(t1, s1)
    preOrder(t2, s2)

    return s2 in s1 # Check if s2 is a substring of s1
