class TwoSum(object):
    def twoSum(self,nums,target):
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

if __name__ == "__main__":
    nums = [1,4,6,7,8,3]
    target = 11
    TwoSum.twoSum(nums,target)

# class Example(object):
#     def run(self):
#         print("Hello, world!")

# if __name__ == '__main__':
#     Example().run()