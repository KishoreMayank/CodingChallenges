'''
Towers of Hanoi:
    Write a function to solve the towers of Hanoi
'''

def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper) # move tower of size n - 1 to helper:
        
        if source: 
            target.append(source.pop()) # move disk from source peg to target peg
        
        hanoi(n - 1, helper, source, target) # move tower of size n-1 from helper to target
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)