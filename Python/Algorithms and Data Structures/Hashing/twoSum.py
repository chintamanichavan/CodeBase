class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            other = target - num 

            if other in seen:
                print([seen[other],index])
                return[seen[other],index]
            else:
                seen[num] = index
        return []
    
nums = [1,3,5,7,9]
target = 8
sol = Solution()
# Solution.twoSum(nums,target) // if you are not using self keyword
sol.twoSum(nums,target)