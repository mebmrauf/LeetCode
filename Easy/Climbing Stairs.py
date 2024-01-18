# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# https://leetcode.com/problems/climbing-stairs/solutions/4584244/solution-for-climbing-stairs-problem/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        totalWays = [0] * (n + 1)
        totalWays[1], totalWays[2] = 1, 2
        for i in range(3, n + 1):
            totalWays[i] = totalWays[i - 1] + totalWays[i - 2]
        return totalWays[n]