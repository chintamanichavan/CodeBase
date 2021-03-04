def containsDuplicate(nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      
      if len(nums) != len(set(nums)):
            return True
      return False 
      #return not len(nums) == len(set(nums))    


nums = [1,2,3,4,5,5,7]
containsDuplicate(nums)