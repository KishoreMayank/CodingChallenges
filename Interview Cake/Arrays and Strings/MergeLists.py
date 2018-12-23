'''
Merge Lists:
    Write a function to merge ordered lists into one sorted list.
    Input:  list1 = [3, 4, 6, 10, 11, 15]
            list2 = [1, 5, 8, 12, 14, 19]
    Output: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
'''
 
def merge_lists(list1, list2):
    merged_size = len(list1) + len(list2)
    merged = [None] * merged_size # initialize a list of len1 + len2

    one = 0
    two = 0
    curr = 0
    while curr < merged_size:
        list1_done = one >= len(list1)
        list2_done = two >= len(list2)
        if (not list1_done and (list2 or list1[one] < list2[two])): # list1 not done and list2 done or greater than
            merged[curr] = list1[one]
            one += 1
        else: 
            merged[curr] = list2[two] # add the element from list2
            two += 1

        curr += 1

    return merged
