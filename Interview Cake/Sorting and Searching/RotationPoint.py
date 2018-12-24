'''
Rotation Point:
    Find the rotation point in an array
'''

def find_rotation_point(nums):

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) / 2
        if nums[mid] > nums[0]: # if the mid is < first elem, then it is still greater than the rotation point 'q' > 'a'
            left = mid + 1
        else: # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            right = mid - 1 

        if left + 1 == right: # boundries have converged and it is on the right
            return right
    
    return -1