'''
Binary Search:
    Binary search
'''

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20], 12))
main()