# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalList = []
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums)-1,
            while left < right:
                totalSum = nums[left] + nums[right] + val
                if totalSum > 0:
                    right -= 1
                elif totalSum < 0:
                    left += 1
                else:
                    finalList.append([nums[left], nums[right], val])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return finalList