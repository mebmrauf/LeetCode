# 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK: return 0
        subarrays = [[]]
        for num in nums:
            if num < minK or num > maxK:
                subarrays.append([])
            else:
                subarrays[-1].append(num)
        
        def countFixedBoundSubarrays(lst):
            if len(lst) == 0 or max(lst) < maxK or min(lst) > minK: return 0
            minIndices, maxIndices = [], []
            for index, num in enumerate(lst):
                if num == minK:
                    minIndices.append(index)
                if num == maxK:
                    maxIndices.append(index)
            result, i, j = 0, 0, 0
            for index, num in enumerate(lst):
                if i < len(minIndices) and minIndices[i] < index:
                    i += 1
                if j < len(maxIndices) and maxIndices[j] < index:
                    j += 1
                if i == len(minIndices) or j == len(maxIndices):
                    break
                result += len(lst) - max(minIndices[i], maxIndices[j])
            return result
        
        return sum(countFixedBoundSubarrays(subarray) for subarray in subarrays)