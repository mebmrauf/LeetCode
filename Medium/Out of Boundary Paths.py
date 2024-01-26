# 576. Out of Boundary Paths
# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod, outCount = 10**9 + 7, 0

        dp = [[0] * n for x in range(m)]
        dp[startRow][startColumn] = 1
        
        for i in range(maxMove):
            dpNew = [[0] * n for y in range(m)]
            for j in range(m):
                for k in range(n):
                    if dp[j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dpNew[j1][k1] = (dpNew[j1][k1] + dp[j][k]) % mod
                            else:
                                outCount = (outCount + dp[j][k]) % mod
            dp = dpNew
        return outCount