# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, left, right = 0, 0, len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                left +=1
            elif sum > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        return count