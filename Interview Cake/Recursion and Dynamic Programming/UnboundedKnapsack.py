'''
Unbounded Knapsack:
    Given a knapsack with a capacity and cakes with a (weight, value), calculate the maximum value 
'''

def unbounded_knapsack(cake_tuples, capacity):
    
    combos = [0] * (capacity + 1)

    for weight, value in cake_tuples:
        if weight == 0 and value > 0:
            return float('inf')
        for i in range(weight, capacity + 1): # for every cake in the range [weight, capacity + 1)
            # take the max of the current or the value at (i - weight) + value
            combos[i] = max(combos[i], combos[i - weight] + value) 
    return combos[capacity]