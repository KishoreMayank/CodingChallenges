'''
Appears Twice:
    Return the number that appears twice in a list of size n + 1 with elements that 
    range from the values of 1...n
'''

def appears_twice(nums):
    if len(nums) < 2:
        raise ValueError()
    
    n = len(nums)
    sum_nums = (n * (n - 1)) / 2 # take the sum of what it should be 
    difference = sum(nums) - sum_nums # take difference to see what is repeated
    return difference