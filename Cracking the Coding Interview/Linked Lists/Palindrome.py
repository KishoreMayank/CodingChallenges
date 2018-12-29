'''
Palindrome:
    Check whether a linked list is a palindrome
'''

def is_palindrome(head):
    fast = slow = head 
    stack = []

    while fast and fast.next: # have a slow and a fast node and add all of the slow nodes to the stack until fast goes out
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast: # if the linked list has an odd number of nodes, move forward by one 
        slow = slow.next

    while slow: # pop out of the stack until the slow node hits the end and check for any discrepenices
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True