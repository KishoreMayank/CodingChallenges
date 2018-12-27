'''
Fibonacci:
    Write a function fib() that takes an integer nn and returns the nnth Fibonacci number
'''

# DYNAMIC PROGRAMMING (BOTTOM - UP)
def fib(n):
    if n < 0:
        raise ValueError('number is less than 0')
    
    if n in [0,1]:
        return n

    prev_prev = 0
    prev = 1
    for _ in range(n - 1): # already have the first two so end at 2 before (n-1 iterations)
        curr = prev + prev_prev # use the previous values to caluclate the current
        prev_prev = prev
        prev = curr
    return curr


# DYNAMIC PROGRAMMING (TOP - DOWN)
memo = {0:0, 1:1}
def fib_td(n):

    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1) + fib(n - 2) # store the value of the fib of the current
        
    return memo[n]
    

