# 930. Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/

from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Count num of subarrays where current sum <= x
        def helper(x):
            if x < 0: return 0
            result, l, currentSum = 0, 0, 0
            for r in range(len(nums)):
                currentSum += nums[r]
                while currentSum > x:
                    currentSum -= nums[l]
                    l += 1
                result += (r - l + 1)
            return result
        return helper(goal) - helper(goal - 1)