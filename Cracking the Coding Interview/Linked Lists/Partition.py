'''
Partition:
    Partition a linked list with all the values less than x to the left and greater than or equal to to the right
'''

def partition(node, x):
    head = tail = node

    while node:
        nextNode = node.next
        if node.value < x: # if a value is less than x, add it to the front
            node.next = head
            head = node
        else: # if a value is greater than x, add it to the back
            tail.next = node
            tail = node
            node.next = None
        node = nextNode
        
    # Error check in case all nodes are less than x
    if tail.next is not None:
        tail.next = None

    return head