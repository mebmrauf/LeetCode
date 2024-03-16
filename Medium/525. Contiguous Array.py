# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one, result, diffIndex = 0, 0, 0, {}
        for i, n in enumerate(nums):
            if n == 1:
                one += 1
            else:
                zero += 1
            if one - zero not in diffIndex:
                diffIndex[one - zero] = i
            if one == zero:
                result = one + zero
            else:
                index = diffIndex[one - zero]
                result = max(result, i - index)
        return result