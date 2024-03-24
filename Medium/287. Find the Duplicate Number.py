# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List
from collections import Counter

# Time complexity and Space complexity both are O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicT = Counter(nums)

        for key, val in dicT.items():
            if val > 1:
                return key
            
# Time complexity O(n) and Space Complexity O(1)
# Floyd's Tortoise and Hare (Cycle Detection) algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return tortoise