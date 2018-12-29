'''
Minimal Tree:
    Given a sorted array of unique integer elements, create a BST with minamal height
'''
class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

def create_min_bst(arr):
    if not arr:
        return None
    mid = (len(arr)) // 2
    root = Node(arr[mid]) # find the current root by looking at the middle of the array
    root.left = create_min_bst(arr[:mid]) # then split the left half
    root.right = create_min_bst(arr[(mid + 1):]) # and split the right half 
    return root # return the root when recursivly going through

