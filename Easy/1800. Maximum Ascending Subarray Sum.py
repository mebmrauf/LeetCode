# 1800. Maximum Ascending Subarray Sum
# https://leetcode.com/problems/maximum-ascending-subarray-sum/

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        leng = len(nums)

        if leng == 1:
            return nums[0]

        currentSum, maxSum = nums[0], nums[0]
        
        for i in range(1, leng):
            if nums[i] > nums[i-1]:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            maxSum = max(maxSum, currentSum)

        return maxSum