# 2958. Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

from typing import List
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        count = Counter()
        answer = 0
        while l < n:
            while r < n and count[nums[r]] < k:
                count[nums[r]] += 1
                r += 1
            answer = max(answer, r - l)
            count[nums[l]] -= 1
            l += 1
        return answer