'''
Magic Index:
    Given a sorted array of distinct integers, write a method to find the magic index
    Magic index: A[i] = i
'''

def magicIndex(arr, start, end): 
    if start > end: # If No Magic Index return -1  
        return -1
  
    midIndex = (start + end) // 2  
    midValue = arr[midIndex]  

    if midIndex == midValue: # Magic Index Found, return it. 
        return midIndex  
  
    left = magicIndex(arr, start, min(midValue, midIndex - 1))  # Search on Left side 
  
    if left >= 0: # If Found on left side, return. 
        return left  
   
    return magicIndex(arr, max(midValue, midIndex + 1), end) # Look for it in the right side.