# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

from typing import List # No need to import in Leetcode

# Time complexity and Space Complexity both are O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicT = {}
        for num in nums:
            if num not in dicT:
                dicT[num] = 1
            else:
                dicT[num] += 1

        maxVal = dicT[nums[0]]
        result = nums[0]
        for key, val in dicT.items():
            if val > maxVal:
                maxVal = val
                result = key
        return result
    
# Time complexity O(n) and Space Complexity O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxElem = None
        count = 0

        # Find the potential majority element
        for num in nums:
            if count == 0:
                maxElem = num
            count += 1 if num == maxElem else -1

        # Verify if the element is the majority element
        count = 0
        for num in nums:
            if num == maxElem:
                count += 1

        return maxElem