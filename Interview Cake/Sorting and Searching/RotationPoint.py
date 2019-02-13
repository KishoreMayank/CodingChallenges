'''
Rotation Point:
    Find the rotation point in an array
'''

def find_rotation_point(nums):

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = int(left + (right - left) / 2)
        mid = (left + right) // 2 # OR THIS - both work for binary search
        if nums[mid] > nums[0]: # if the mid is < first elem, then it is still greater than the rotation point 'q' > 'a'
            left = mid + 1
        else: # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            right = mid - 1 

        if left + 1 == right: # boundries have converged and it is on the right
            return right
    
    return -1

def main():
    print(find_rotation_point([3,4,5,1,2]))

main()