# 3151. Special Array I
# https://leetcode.com/problems/special-array-i/

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        leng = len(nums)
        if leng == 1:
            return True
        for i in range(1, leng):
            if (nums[i-1]%2 == 0 and nums[i]%2 == 0) or (nums[i-1]%2 != 0 and nums[i]%2 != 0):
                return False
        return True