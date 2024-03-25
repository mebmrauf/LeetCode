# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] *= -1
        return duplicates