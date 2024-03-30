# 992. Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/

from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def temp(nums, k):
            visited = [0] * (len(nums) + 1)
            count, result, l, r = 0, 0, 0, 0
            m = 0
            while True:
                m += 1
                while count < k and r < len(nums):
                    if visited[nums[r]] == 0: count += 1
                    visited[nums[r]] += 1
                    r += 1
                if count < k: break
                result += len(nums) - r + 1
                visited[nums[l]] -= 1
                if visited[nums[l]] == 0: count -= 1
                l += 1
            return result
        return temp(nums, k) - temp(nums, k+1)