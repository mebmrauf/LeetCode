# 2364. Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

from typing import List
from collections import defaultdict

# Brute Force Approach (TLE Issue)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        leng, count = len(nums), 0
        
        for i in range(leng):
            num1 = nums[i] - i
            for j in range(i+1, leng):
                num2 = nums[j] - j
                if num2 != num1:
                    count += 1
        
        return count
    

# HashMap
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalPairs = n * (n - 1) // 2
        freq, goodPairs = defaultdict(int), 0
        
        for i, num in enumerate(nums):
            key = num - i
            goodPairs += freq[key]
            freq[key] += 1
        
        return totalPairs - goodPairs 