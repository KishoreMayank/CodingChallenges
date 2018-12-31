'''
Triple Step:
    A child can run up and hop 1, 2, or 3 steps at a time. How many ways can it make it up the stairs
'''

# DYNAMIC PROGRAMMING (TOP - DOWN)
memo = {0:1, 1:1, 2:2}
def triple_step(n):

    if n in memo:
        return memo[n]
    memo[n] = triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3) # store the number of ways to get to this step
        
    return memo[n]

def main():
    print(triple_step(5))

main()