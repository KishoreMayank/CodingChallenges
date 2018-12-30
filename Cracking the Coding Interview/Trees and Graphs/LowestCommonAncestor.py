'''
Lowest Common Ancestor:
    Lowest common ancestor of two nodes in a binary tree
'''

def findLCA(root, n1, n2): 
      
    if not root: # if you reach the end of the tree, return None to go back up
        return None
  
    if root.value == n1 or root.value == n2: # check to see if it has hit a target, if it has, set the left/right to that value
        return root  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
  
    if left_lca and right_lca: # only if both elements are in the same tree, then return the root of both
        return root  
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca 