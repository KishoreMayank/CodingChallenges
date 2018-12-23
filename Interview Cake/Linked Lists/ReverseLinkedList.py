'''
Reverse Linked List:
    Write a function to reverse a linked list
'''

def reverse(head):
    curr = head
    prev = None
    next_node = None

    while curr: # iterate till the end 
        next_node = curr.next # copy pointer to next node
        curr.next = prev # Reverse the 'next' pointer
        prev = curr # Step forward in the list
        curr = next_node

    return prev


