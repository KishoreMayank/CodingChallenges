'''
 Contains Cycle:
    Write a function  that takes the first node in a singly-linked list and returns a boolean
    indicating whether the list contains a cycle.
'''
 
def contains_cycle(head):
    slow = head # slow node will iterate one at a time
    fast = head # fast node will iterate two at a time 

    while fast is not None and fast.next is not None: # Loop till we hit the end of the list
        slow = slow.next
        fast = fast.next.next
        if fast is slow: # if fast intersects with slow
            return True
    
    return False # if fast is None
    


