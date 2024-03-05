# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, sets = 0, set(nums)
        for num in sets:
            if num-1 not in sets:
                l = 0
                while num+l in sets:
                    l += 1
                longest = max(longest, l)
        return longest