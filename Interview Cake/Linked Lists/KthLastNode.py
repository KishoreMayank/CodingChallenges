'''
Kth Last Node:
    Finds the kth last node
'''


def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError('Impossible to find less than first to last node: %s' % k)

    left  = head
    right = head

    for _ in range(k - 1): # Move right to the kth node
        if not right.next:
            raise ValueError('k is larger than the length of the linked list: %s' % k)
        right = right.next

    while right.next: # move the left and the right until the right hits the end
        left  = left.next
        right = right.next

    return left


