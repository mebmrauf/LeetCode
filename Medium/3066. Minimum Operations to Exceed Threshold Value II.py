# 3066. Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0

        while nums[0] < k:
            maxMin1 = heappop(nums)
            maxMin2 = heappop(nums)
            newNum = maxMin1 * 2 + maxMin2
            heappush(nums, newNum)
            operations += 1

        return operations