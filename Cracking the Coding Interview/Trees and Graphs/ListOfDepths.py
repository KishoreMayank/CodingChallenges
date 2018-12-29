'''
List of Depths:
    Create a linked list the of nodes at each depth
'''
class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.next = None
        self.val = item

def list_of_depths(root):

    queue = []
    queue.append(root)
    queue.append(None) # append a None to signify the end of the level

    while queue:
        curr = queue.pop(0)
        if curr: 
            curr.next = queue[0] # if it is not none, set the next pointer to the new top of the queue
            if curr.left:
                queue.append(curr.left) # append the left
            if curr.right:
                queue.append(curr.right) # append the right
        elif queue:
            queue.append(None) # if it is None, set the new end to the level
        