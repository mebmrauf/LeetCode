# 2962. Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum, maxCount = max(nums), 0
        l, result = 0, 0
        for r in range(len(nums)):
            if nums[r] == maxNum:
                maxCount += 1
            while maxCount > k or ( l <= r and maxCount == k and nums[l] != maxNum):
                if nums[l] == maxNum:
                    maxCount -= 1
                l += 1
            if maxCount == k:
                result += l + 1
        return result