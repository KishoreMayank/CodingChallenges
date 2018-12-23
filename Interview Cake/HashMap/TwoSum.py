'''
Two Sum:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    Input: [2, 7, 11, 15], target = 9
    Output: [0, 1]
'''

def twoSum(nums, target):
    buff_dict = {} 
    for i in range(len(nums)): 
        if nums[i] in buff_dict: # if the other time exists to get to target, return that index with the current 
            return [buff_dict[nums[i]], i]
        buff_dict[target - nums[i]] = i # put the required time to get to target (target - curr_time) in the map
    return None
