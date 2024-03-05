# 446. Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  # Increment the count of subsequences with the same difference
                if diff in dp[j]:  # If there are previous subsequences with the same difference
                    dp[i][diff] += dp[j][diff]  # Add them to the count of subsequences ending at index i
                    total_count += dp[j][diff]  # Update the total count

        return total_count