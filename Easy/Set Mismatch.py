# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l, nums, array = len(nums), Counter(nums), [0]*2
        for num in range(1, l+1):
            if nums[num] == 2:
                array[0] = num
            elif num not in nums:
                array[1] = num
        return array