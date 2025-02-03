# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        leng = len(nums)

        if leng == 1:
            return 1
        
        increase, decrease, maxLen = 1, 1, 1
        
        for i in range(leng - 1):
            if nums[i] > nums[i+1]:
                decrease, increase = decrease + 1, 1
            elif nums[i] < nums[i+1]:
                increase, decrease = increase + 1, 1
            else:
                increase, decrease = 1, 1

            maxLen = max(maxLen, increase, decrease)

        return maxLen