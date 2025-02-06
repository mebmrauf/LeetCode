# 1726. Tuple with Same Product
# https://leetcode.com/problems/tuple-with-same-product/

from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dicT = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i]*nums[j]
                if product not in dicT:
                    dicT[product] = 1
                else:
                    dicT[product] += 1

        count = 0
        for c in dicT.values():
            if c > 1:
                count += c * (c - 1) * 4

        return count