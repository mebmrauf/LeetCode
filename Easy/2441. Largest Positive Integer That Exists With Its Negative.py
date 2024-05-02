# 2441. Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        maxK = -1
        
        for num in nums:
            if -num in seen:
                maxK = max(maxK, abs(num))
            seen.add(num)
        
        return maxK if maxK != -1 else -1