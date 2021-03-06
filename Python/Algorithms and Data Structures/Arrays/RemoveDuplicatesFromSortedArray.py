from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1
    
    # nums = [0,0,1,1,1,2,2,3,3,4]
    j = 1 # slower pointer, only move when meet unique number
    for i in range(1, len(nums)): # faster pointer, i will iterate over all element in nums
        print(i)
        if nums[i] != nums[i-1]: # when nums[i] is a unique number, assign it to nums[j]
            nums[j] = nums[i]
            print(nums)
            j += 1
    # After for loop, i = 9, j = 5, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    # We have to delete duplicates backwards
    print(j)
    for delete_index in range(i, j-1, -1):
        del nums[delete_index]
    print(nums)
    return j

#nums = [0,1,2,3,3,3]
nums = [0,0,1,1,2,2,3,3]
removeDuplicates(nums)