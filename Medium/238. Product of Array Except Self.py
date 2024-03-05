# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct, rightProduct, l= 1, 1, len(nums)
        result = [1] * l

        for i in range(l):
            result[i] *= leftProduct
            leftProduct *= nums[i]

        for i in range(l - 1, -1, -1):
            result[i] *= rightProduct
            rightProduct *= nums[i]

        return result