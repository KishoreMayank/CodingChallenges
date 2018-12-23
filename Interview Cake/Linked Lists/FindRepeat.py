'''
Find Repeat:
    We can find a duplicate integer in O(n) time while keeping our space cost at O(1).
'''

def find_duplicate(int_list):
    n = len(int_list) - 1

    # STEP 1: GET INSIDE A CYCLE
    # Start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    curr = n + 1
    for _ in range(n):
        curr = int_list[curr - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a list is *index* 1

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # Find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    curr_in_cycle = curr
    current_curr = int_list[curr - 1]  # 1 step ahead
    count = 1
    while current_curr != curr_in_cycle:
        current_curr = int_list[current_curr - 1]
        count += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # Start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    slow = n + 1
    fast = n + 1
    for _ in range(count):
        fast = int_list[fast - 1]

    # Advance until the pointers are in the same position
    # which is the first node in the cycle
    while slow != fast:
        slow = int_list[slow - 1]
        fast = int_list[fast - 1]

    # Since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return slow


