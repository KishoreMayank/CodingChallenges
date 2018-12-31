'''
Recursive Multiply:
    Write a function to recursivly multiply without the * operator
'''

def minProduct(a,b):
    bigger = b if a < b else a #a < b ? b : a
    smaller = a if a < b else b #a < b ? a : b
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0: # base case
        return 0
    elif smaller == 1: # base case
        return bigger
        
    s = smaller >> 1 # divide the smaller by two

    halfProd = minProductHelper(s,bigger) # keep recursively calling until a base case
    if smaller % 2 == 0:
        return halfProd + halfProd # if smaller is even add both
    else:
        return halfProd + halfProd + bigger # if smaller is odd add both and half of the other

print(minProduct(5,10))