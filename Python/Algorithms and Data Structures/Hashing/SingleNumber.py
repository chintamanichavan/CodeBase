from collections import defaultdict
from typing import List

def singleNumber(nums: List[int]) -> int:
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i

nums = [4,1,2,1,2]
singleNumber(nums)