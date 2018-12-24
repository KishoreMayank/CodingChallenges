'''
Highest Product of Three:
    Given a list of integers, find the highest product you can get from three of the integers
'''

def highest_prod_3(ints):
    if len(ints) < 3:
        raise ValueError('Less than 3 items!')

    highest = max(ints[0], ints[1])
    lowest  = min(ints[0], ints[1])
    high_2 = ints[0] * ints[1]
    low_2  = ints[0] * ints[1]
    high_3 = ints[0] * ints[1] * ints[2] # first three numbers

    for i in range(2, len(ints)):
        curr = ints[i]

        # update the highest prods
        high_3 = max(high_3, curr * high_2, curr * low_2)
        high_2 = max(high_2, curr * highest, curr * lowest)
        low_2 = min(low_2, curr * highest, curr * lowest)

        highest = max(highest, curr)
        lowest = min(lowest, curr)

    return high_3