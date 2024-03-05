# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expSum, actSum = (n*(n+1)) // 2, sum(nums)
        return expSum - actSum