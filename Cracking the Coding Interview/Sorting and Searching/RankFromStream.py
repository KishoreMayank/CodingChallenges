'''
Rank from Stream:
    Keep track of the number of integers less than the asked for number 
'''

class Node:
    def __init__(self):
        self.data
        self.left
        self.right
        self.leftSize
  
def newNode(data):
    temp = Node()
    temp.data = data
    temp.left = temp.right = None
    temp.leftSize = 0
    return temp
  
# Inserting a new Node. 
def insert(root, data): 
    if not root :
        return newNode(data)
  
    # Updating size of left subtree. 
    if data <= root.data:
        root.left = insert(root.left, data)
        root.leftSize += 1
    else:
        root.right = insert(root.right, data)
    return root 
  
# Function to get Rank of a Node x. 
def getRank(root, x): 
    # Step 1 
    if root.data == x: 
        return root.leftSize
  
    # Step 2. 
    if x < root.data: 
        if not root.left: 
            return -1 
        else:
            return getRank(root.left, x)
  
    # Step 3. 
    else: 
        if not root.right: 
            return -1
        else:
            rightSize = getRank(root.right, x)
            return root.leftSize + 1 + rightSize 