# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result, left, right = [0]*l, 0, l-1
        for i in range(l-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left]**2
                left += 1
            else:
                result[i] = nums[right]**2
                right -= 1
        return result