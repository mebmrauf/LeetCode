# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        leng = len(nums)

        for i in range(leng):
            if nums[i] > nums[(i+1)%leng]:
                count += 1
                if count > 1:
                    return False
        return True