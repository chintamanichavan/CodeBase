def twoSum(nums,target):
    result = []
    numsMap = {}
    for i in range(len(nums)):
        numsMap[nums[i]] = i
    for i in nums:
        if numsMap.has_key(target - nums[i]):
            result.append(nums[i])
            result.append(target - nums[i])
    print(result)
    return result

nums = [1,4,6,7,8,3]
target = 11
twoSum(nums,target)