'''
Cycle Beginning:
    Write a function  that takes the first node in a singly-linked list and returns a boolean
    indicating whether the list contains a cycle.
'''
 
def cycle_beginning(head):
    slow = fast = head

    while fast is not None and fast.next is not None: # Loop till we hit the end of the list
        slow = slow.next
        fast = fast.next.next
        if fast is slow: # if fast intersects with slow
            break

    if fast is None or fast.next is None: # if there is no cycle
        return None

    slow = head
    while slow != fast: # ball and stick method to move forward
        slow = slow.next
        fast = fast.next

    return fast

    
def removeLoop(head, slow):
    ptr1 = ptr2 = slow

    k = 1
    while ptr1.next != ptr2: # Count the number of nodes in loop 
        ptr1 = ptr1.next
        k +=1

    ptr1 = ptr2 = head
    for _ in range(k): # move the pointer 
        ptr2 = ptr2.next
    
    while ptr2 != ptr1: # Move both pointers at the same place they will meet at loop starting node
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    ptr2 = ptr2.next
    while(ptr2.next != ptr1): # Get pointer to the last node before the start
        ptr2 = ptr2.next
    
    ptr2.next = None  # delete the loop