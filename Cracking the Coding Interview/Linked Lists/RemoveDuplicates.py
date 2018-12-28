'''
Remove Duplicates:
    How to remove duplicates from an unsorted list
'''

def remove_dups(llist):
    if llist.head is None:
        return

    curr = llist.head
    seen = set([curr.value]) # keep a set of all of the values that have been seen
    while curr.next:
        if curr.next.value in seen: # if it is in seen, remove it
            curr.next = curr.next.next
        else:
            seen.add(curr.next.value)
            curr = curr.next

    return llist