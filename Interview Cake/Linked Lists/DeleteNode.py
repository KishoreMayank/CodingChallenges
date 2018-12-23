'''
Delete Node:
    Delete a node from a singly-linked list, given only a variable pointing to that node.
'''

def delete_node(node):
    next_node = node.next
    if next_node:
        node.value = next_node.value
        node.next  = next_node.next
    else:
        raise Exception("Can't delete the last node with this technique!")