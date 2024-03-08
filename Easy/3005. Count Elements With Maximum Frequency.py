# 3005. Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else: dic[i] += 1
        maxVal = 1
        for val in dic.values():
            if maxVal < val:
                maxVal = val
        count = 0
        for val in dic.values():
            if maxVal == val:
                count += 1
        return maxVal*count
    
# OR
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        maxVal = max(dic.values())
        count = 0
        for val in dic.values():
            if maxVal == val: count += 1
        return maxVal*count