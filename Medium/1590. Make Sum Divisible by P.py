# 1590. Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalSum = sum(nums)
        remaining = totalSum % p

        if remaining == 0:
            return 0
        
        preMod = {0: -1}
        currentPrefix = 0
        minLen = len(nums)
        
        for i, num in enumerate(nums):
            currentPrefix = (currentPrefix + num) % p
            target = (currentPrefix - remaining) % p
            
            if target in preMod:
                minLen = min(minLen, i - preMod[target])
            preMod[currentPrefix] = i

        return minLen if minLen < len(nums) else -1
