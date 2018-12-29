'''
Sort Stack:
    The smallest items will be on the top using only stacks
'''

def sort_stack(stack):
    r = []
    while stack:
        temp = stack.pop()
        while r and r[-1] > temp: # check if the top of the sorted stack is greater than the top of the given stack
            stack.append(r.pop()) # if it is, then push the top of the sorted stack into the given stack
        r.append(temp) # always push in the temp into the sorted stack
    
    while r:
        stack.append(r.pop()) # this will make it least to greatest