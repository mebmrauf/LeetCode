# 1043. Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            maximum = 0
            for j in range(i, -1, -1):
                if i - j >= k: break
                maximum = max(maximum, arr[j])
                dp[i+1] = max(dp[i+1], dp[j] + (i - j + 1) * maximum)
        return dp[-1]