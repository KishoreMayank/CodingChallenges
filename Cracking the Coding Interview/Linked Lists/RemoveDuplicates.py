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
        if curr.next.value in seen: # if the next is a duplicate
            curr.next = curr.next.next # move the next pointer past the duplicate value
        else:
            seen.add(curr.next.value) # otherwise add it to the set
            curr = curr.next # and move past all of the subsequent duplicates

    return llist