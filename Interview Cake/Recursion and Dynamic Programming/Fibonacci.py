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
    for _ in range(n - 1):
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
    return curr


# DYNAMIC PROGRAMMING (TOP - DOWN)
memo = {0:0, 1:1}
def fib_td(n):

    # Compute the nth Fibonacci number
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
        
    return memo[n]
    

