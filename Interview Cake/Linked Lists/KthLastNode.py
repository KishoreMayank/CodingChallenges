'''
Kth Last Node:
    Finds the kth last node
'''


def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError('Impossible to find less than first to last node: %s' % k)

    left_node  = head
    right_node = head

    for _ in range(k - 1): # Move right_node to the kth node
        if not right_node.next:
            raise ValueError('k is larger than the length of the linked list: %s' % k)
        right_node = right_node.next

    while right_node.next: # move the left and the right until the right hits the end
        left_node  = left_node.next
        right_node = right_node.next

    return left_node


