# 1. Two Sum (Easy)
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), i]
            
            num_set.add(num)

        return []