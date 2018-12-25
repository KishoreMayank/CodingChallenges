'''
Super Balanced:
    A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.
'''

def super_balanced(root):
    if not root:
        return False

    depths = []

    nodes = [] # initialize the stack for dfs
    nodes.append((root, 0)) # use a tuple to keep track of the node and depth

    while len(nodes):
        node, depth = nodes.pop()
        if (not node.left) and (not node.right):
            depths.append(depth)
            if (len(depths) > 2) or (len(depths) == 2 and 
            abs(depths[1] - depths[0]) > 1): 
                return False # if more than two elements or difference is greater than 1
        else:
            if node.left:
                nodes.append(node.left, depth + 1)
            if node.right:
                nodes.append(node.right, depth + 1)
    return True
