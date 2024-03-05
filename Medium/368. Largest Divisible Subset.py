# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        
        # dp[i] represents the length of the largest divisible subset ending at nums[i]
        dp = [1] * n
        
        # parent[i] represents the index of the previous element in the largest divisible subset ending at nums[i]
        parent = [-1] * n
        
        max_length, max_index = 1, 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    
                    if dp[i] > max_length:
                        max_length = dp[i]
                        max_index = i
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]