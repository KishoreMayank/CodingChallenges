'''
Intersection:
    Determine if and where two linked lists intersect
'''

def intersection(list1, list2):
    if list1.tail is not list2.tail: # checking whether the tails are equal
        return False

    s = list1 if len(list1) < len(list2) else list2
    l = list2 if len(list1) < len(list2) else list1

    diff = len(l) - len(s) # finding the difference between the lengths of the two lists

    s_node, l_node = s.head, l.head

    for _ in range(diff): # move the longer node diff steps forward to match length
        l_node = l_node.next

    while s_node is not l_node: # keep going through until intersection is found
        s_node = s_node.next
        l_node = l_node.next

    return l_node