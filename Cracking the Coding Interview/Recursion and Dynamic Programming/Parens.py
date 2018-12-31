'''
Parens:
    Implement an algorithm to print all valid combos of n pairs of parentheses
'''

def parens(n):
    if n <= 0:
        return ['']
    else:
        combos = []
        helper('', n, n, combos)
        return combos


def helper(string, left, right, combos):
    if left <= 0 and right <= 0: # if you have run out of open (left) and close (right) parens, append the string
        combos.append(string)
    else:
        if left > 0: # if you still have left
            helper(string + '(', left - 1, right, combos)
        if right > left and right > 0: # add a right
            helper(string + ')', left, right - 1, combos)
  
n = 3
print(parens(n))


