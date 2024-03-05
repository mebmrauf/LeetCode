# 2971. Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result, current = -1, 0
        for num in nums:
            if current > num:
                result = max(result, current + num)
            current += num
        return result